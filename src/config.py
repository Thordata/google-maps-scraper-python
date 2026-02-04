"""
Google Maps spider configuration.

Strictly aligned with spider_id list in the official documentation:

Details spiders
- google_map-details_by-url
- google_map-details_by-cid
- google_map-details_by-location
- google_map-details_by-placeid

Reviews spiders
- google_comment_by-url
"""

SPIDER_CONFIG = {
    # ========================
    # 1. Details spiders
    # ========================
    # cURL: spider_id=google_map-details_by-url
    "details_by_url": {
        "id": "google_map-details_by-url",
        "name": "google.com",
        "desc": "Deep scrape business details by Google Maps URL",
    },
    # cURL: spider_id=google_map-details_by-cid
    "details_by_cid": {
        "id": "google_map-details_by-cid",
        "name": "google.com",
        "desc": "Deep scrape business details by CID",
    },
    # cURL: spider_id=google_map-details_by-location
    "details_by_location": {
        "id": "google_map-details_by-location",
        "name": "google.com",
        "desc": "Deep scrape business details by geo location and keyword",
    },
    # cURL: spider_id=google_map-details_by-placeid
    "details_by_placeid": {
        "id": "google_map-details_by-placeid",
        "name": "google.com",
        "desc": "Deep scrape business details by place_id",
    },
    # ========================
    # 2. Reviews spiders
    # ========================
    # cURL: spider_id=google_comment_by-url
    "reviews_by_url": {
        "id": "google_comment_by-url",
        "name": "google.com",
        "desc": "Scrape user reviews by Google Maps URL with date limits",
    },
}

# Default task settings (can be adjusted if needed)
DEFAULT_TIMEOUT = 600
POLL_INTERVAL = 3