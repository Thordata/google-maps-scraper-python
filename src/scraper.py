# src/scraper.py
import os
import logging
import json
from typing import List, Dict, Any, Union
from thordata import ThordataClient
from .config import SPIDER_CONFIG, DEFAULT_TIMEOUT, POLL_INTERVAL

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("GoogleMapsScraper")

class GoogleMapsScraper:
    def __init__(self):
        self.api_key = os.getenv("THORDATA_SCRAPER_TOKEN")
        # Task API 需要 public token
        self.public_token = os.getenv("THORDATA_PUBLIC_TOKEN")
        self.public_key = os.getenv("THORDATA_PUBLIC_KEY")
        
        if not self.api_key:
            raise ValueError("THORDATA_SCRAPER_TOKEN is required in .env")

        self.client = ThordataClient(
            scraper_token=self.api_key,
            public_token=self.public_token,
            public_key=self.public_key
        )

    def _run_task_mode(self, mode: str, params: Dict[str, Any]) -> Dict:
        """运行 Web Scraper Task (用于 Details 和 Reviews)"""
        cfg = SPIDER_CONFIG[mode]
        logger.info(f"🚀 Starting Task: {cfg['desc']} (ID: {cfg['id']})")
        
        try:
            # 自动轮询直到完成
            result_url = self.client.run_task(
                file_name=f"gmaps_{mode}_{os.getpid()}",
                spider_id=cfg["id"],
                spider_name=cfg["name"],
                parameters=params,
                max_wait=DEFAULT_TIMEOUT,
                initial_poll_interval=POLL_INTERVAL
            )
            
            logger.info(f"✅ Task Finished. Downloading data...")
            
            # 下载并解析 JSON
            import requests
            response = requests.get(result_url)
            try:
                return response.json()
            except:
                return {"raw_data": response.text}
                
        except Exception as e:
            logger.error(f"❌ Task Failed: {e}")
            return {"error": str(e)}

    def search_businesses(self, keyword: str, limit: int = 20) -> Dict:
        """
        [Hybrid Mode] 使用 SERP API 进行搜索 (速度快)
        """
        logger.info(f"🔍 Searching via SERP API: '{keyword}'")
        try:
            # 使用 SDK 的 SERP 接口
            # engine="google_maps" 是 SDK 标准支持的
            data = self.client.serp_search(
                query=keyword,
                engine="google_maps",
                type="search",
                num=limit
            )
            return data
        except Exception as e:
            logger.error(f"❌ Search Failed: {e}")
            return {"error": str(e)}

    def get_details(self, url: str) -> Dict:
        """
        使用 Web Scraper 获取详情
        Param: url (Google Maps URL)
        """
        # 对应 cURL: {"url": "..."}
        params = {"url": url}
        return self._run_task_mode("details", params)

    def get_reviews(self, url: str, days_limit: int = 0) -> Dict:
        """
        使用 Web Scraper 获取评论
        Param: url, days_limit (Optional)
        """
        # 对应 cURL: {"url": "...", "days_limit": "10"}
        params = {"url": url}
        if days_limit > 0:
            params["days_limit"] = str(days_limit)
            
        return self._run_task_mode("reviews", params)