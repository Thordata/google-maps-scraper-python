# src/config.py

# 真实 Spider ID 配置 (基于 Dashboard cURL)
SPIDER_CONFIG = {
    # 1. 搜索功能 (使用 SERP API，不需要 Spider ID)
    "search": {
        "engine": "google_maps",
        "desc": "Search businesses using SERP API (Fast & Sync)"
    },
    
    # 2. 详情功能 (使用 Web Scraper Task)
    # cURL: spider_id=google_map-details_by-url
    "details": {
        "id": "google_map-details_by-url",
        "name": "google.com",
        "desc": "Deep scrape business details"
    },
    
    # 3. 评论功能 (使用 Web Scraper Task)
    # cURL: spider_id=google_comment_by-url
    "reviews": {
        "id": "google_comment_by-url",
        "name": "google.com",
        "desc": "Scrape user reviews with date limits"
    }
}

# 默认设置
DEFAULT_TIMEOUT = 600
POLL_INTERVAL = 3