import json
import logging
import os
from typing import Any, Dict, List, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from thordata import ThordataClient
from thordata.exceptions import ThordataNetworkError

from .config import DEFAULT_TIMEOUT, POLL_INTERVAL, SPIDER_CONFIG

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("GoogleMapsScraper")


class GoogleMapsScraper:
    def __init__(self):
        self.api_key = os.getenv("THORDATA_SCRAPER_TOKEN")
        # Task API requires public token as well
        self.public_token = os.getenv("THORDATA_PUBLIC_TOKEN")
        self.public_key = os.getenv("THORDATA_PUBLIC_KEY")

        if not self.api_key:
            raise ValueError("THORDATA_SCRAPER_TOKEN is required in .env")

        self.client = ThordataClient(
            scraper_token=self.api_key,
            public_token=self.public_token,
            public_key=self.public_key,
        )

        # Reuse the same HTTP session & retry strategy as AmazonScraper
        self._http = requests.Session()
        retry = Retry(
            total=5,
            connect=5,
            read=5,
            backoff_factor=0.6,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._http.mount("https://", adapter)
        self._http.mount("http://", adapter)

    # ========================
    # Common task execution & download helpers
    # ========================
    def _download_json(self, url: str) -> Any:
        resp = self._http.get(url, timeout=60)
        resp.raise_for_status()

        text = resp.text.strip()
        if not text:
            raise ValueError("Empty response from server")

        try:
            return resp.json()
        except json.JSONDecodeError as e:
            # Support NDJSON / multi-line JSON
            try:
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                if not lines:
                    raise ValueError("No valid JSON lines found")

                parsed = [json.loads(line) for line in lines]
                if len(parsed) == 1:
                    return parsed[0]
                return parsed
            except (json.JSONDecodeError, ValueError):
                logger.error(f"Failed to parse JSON response: {e}")
                logger.error(f"Response text (first 500 chars): {text[:500]}")
                raise

    def _run(self, mode: str, params: Union[Dict[str, Any], List[Dict[str, Any]]]) -> Any:
        cfg = SPIDER_CONFIG.get(mode)
        if not cfg:
            raise ValueError(f"Invalid mode: {mode}")

        logger.info(f"Google Maps {mode}: {cfg['desc']} (spider_id={cfg['id']})")

        try:
            # Do not re-encode the URL here; parameters are passed as-is to the SDK
            # so that `%26` / `&` are handled only once inside the SDK.
            result_url = self.client.run_task(
                file_name=f"gmaps_{mode}_{os.getpid()}",
                spider_id=cfg["id"],
                spider_name=cfg["name"],
                parameters=params,
                max_wait=DEFAULT_TIMEOUT,
                initial_poll_interval=POLL_INTERVAL,
            )
            logger.info("✅ Task finished. Downloading result JSON...")
            return self._download_json(result_url)

        except Exception as e:
            task_id = "N/A"
            if isinstance(e, ThordataNetworkError):
                msg = str(e)
                if msg.startswith("Task "):
                    parts = msg.split()
                    if len(parts) > 1:
                        task_id = parts[1]

            error_details = {
                "error": str(e),
                "error_type": type(e).__name__,
                "task_id": task_id,
                "spider_id": cfg["id"],
                "parameters": params,
            }
            logger.error(f"Google Maps scraping task failed: {error_details}")
            return error_details

    # ========================
    # SERP search (keep original public API)
    # ========================
    def search_businesses(self, keyword: str, limit: int = 20) -> Any:
        """
        [Hybrid Mode] Use SERP API to search businesses (fast, synchronous).
        """
        logger.info(f"🔍 Searching via SERP API: '{keyword}'")
        try:
            data = self.client.serp_search(
                query=keyword,
                engine="google_maps",
                type="search",
                num=limit,
            )
            return data
        except Exception as e:
            logger.error(f"❌ Search Failed: {e}")
            return {"error": str(e)}

    # ========================
    # 1. Details spiders
    # ========================
    def details_by_url(self, params: Union[Dict[str, Any], List[Dict[str, Any]]]) -> Any:
        """
        Matches official cURL:
        spider_id=google_map-details_by-url
        spider_parameters=[{"url": "https://www.google.com/maps/place/..."}]
        """
        return self._run("details_by_url", params)

    def details_by_cid(self, params: Union[Dict[str, Any], List[Dict[str, Any]]]) -> Any:
        """
        Matches official cURL:
        spider_id=google_map-details_by-cid
        spider_parameters=[{"CID": "2476046430038551731"}]
        """
        return self._run("details_by_cid", params)

    def details_by_location(self, params: Union[Dict[str, Any], List[Dict[str, Any]]]) -> Any:
        """
        Matches official cURL:
        spider_id=google_map-details_by-location
        spider_parameters=[{
            "country": "United States",
            "keyword": "pizza",
            "lat": "33",
            "long": "118",
            "zoom_level": "25"
        }]
        """
        return self._run("details_by_location", params)

    def details_by_placeid(self, params: Union[Dict[str, Any], List[Dict[str, Any]]]) -> Any:
        """
        Matches official cURL:
        spider_id=google_map-details_by-placeid
        spider_parameters=[{"place_id": "..."}, {"place_id": "..."}]
        """
        return self._run("details_by_placeid", params)

    # Backward compatible helper: single-URL details
    def get_details(self, url: str) -> Any:
        """
        Get details for a single Google Maps URL (backward compatible helper).
        Param: url (Google Maps URL)
        """
        params: Dict[str, Any] = {"url": url}
        # Pass raw dict; SDK will take care of encoding to avoid double-encoding.
        return self.details_by_url(params)

    # ========================
    # 2. Reviews spiders
    # ========================
    def reviews_by_url(self, params: Union[Dict[str, Any], List[Dict[str, Any]]]) -> Any:
        """
        Matches official cURL:
        spider_id=google_comment_by-url
        spider_parameters=[{"url": "...", "days_limit": "10"}]
        """
        return self._run("reviews_by_url", params)

    # Backward compatible helper: single-URL reviews
    def get_reviews(self, url: str, days_limit: int = 0) -> Any:
        """
        Get reviews for a single Google Maps URL (backward compatible helper).
        Param: url, days_limit (Optional)
        """
        params: Dict[str, Any] = {"url": url}
        if days_limit > 0:
            params["days_limit"] = str(days_limit)

        return self.reviews_by_url(params)