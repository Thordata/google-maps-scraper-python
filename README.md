# Google Maps Scraper for Python

<div align="center">

<img src="https://img.shields.io/badge/Thordata-Official-blue?style=for-the-badge" alt="Thordata Logo">

**Extract leads, emails, phones, and reviews from Google Maps at scale.**  
*Powered by Thordata's high-performance AI infrastructure.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![API Status](https://img.shields.io/badge/API-Stable-success)](https://www.thordata.com/)

</div>

---

## ⚡ Features

*   **🔍 Hybrid Search**: Fast listing search via SERP API.
*   **🏢 Deep Details**: Extract website, phone, opening hours, and claimed status.
*   **⭐ Review Extraction**: Scrape user reviews, ratings, and post dates.
*   **🚀 No Browser Needed**: 100% Cloud-based. No Selenium/Puppeteer maintenance.
*   **🛡️ Enterprise Grade**: Automatic IP rotation, CAPTCHA solving, and retry logic.

## 📦 Sample Output

```json
[
  {
    "fid_location": "0x47a5f50c083530a3:0xfdba8746b538141",
    "place_id": "ChIJozA1CAz1pUcRQYFTa3So2w8",
    "url": "https://www.google.com/maps?q=place_id:ChIJozA1CAz1pUcRQYFTa3So2w8",
    "country": "",
    "lat": 52.126308599999994,
    "lon": 11.609474299999999,
    "category": "Restaurant",
    "address": "Winckelmannstraße 16 39108 Magdeburg Germany ",
    "business_details": [
      {
        "field_name": "storefront_googblue_24dp",
        "details": "Pizza Inn Magdeburg",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/storefront_googblue_24dp.png"
      },
      {
        "field_name": "category_googblue_24dp",
        "details": "Restaurant",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/category_googblue_24dp.png"
      },
      {
        "field_name": "location_on_googblue_24dp",
        "details": "Winckelmannstraße 16, 39108 Magdeburg, Germany",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/location_on_googblue_24dp.png"
      },
      {
        "field_name": "schedule_googblue_24dp",
        "details": "Closed · Opens 5 PM",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/schedule_googblue_24dp.png"
      },
      {
        "field_name": "call_googblue_24dp",
        "details": "+49 391 50963059",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/call_googblue_24dp.png"
      },
      {
        "field_name": "public_googblue_24dp",
        "details": "http://www.pizza-inn-md.de/content/karte_ph_2024.png",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/public_googblue_24dp.png"
      },
      {
        "field_name": "location_off_googblue_24dp",
        "details": "Place is closed or not here",
        "link": "https://www.gstatic.com/images/icons/material/system_gm/2x/location_off_googblue_24dp.png"
      }
    ],
    "services_provided": [
      "Kerbside pickup",
      "No-contact delivery",
      "Delivery",
      "Takeaway",
      "Dine-in",
      "Solo dining",
      "Late-night food",
      "Quick bite",
      "Lunch",
      "Dinner",
      "Casual",
      "LGBTQ+ friendly",
      "Transgender safe space"
    ],
    "name": "Pizza Inn Magdeburg",
    "main_image": "",
    "rating": "4.8",
    "reviews": "72",
    "reviews_count": "72",
    "type": "Restaurant",
    "service_options": [
      "Dine-in",
      "Kerbside pickup",
      "No-contact delivery"
    ],
    "open_hours": {},
    "open_website": "http://www.pizza-inn-md.de/content/karte_ph_2024.png",
    "video_links": "",
    "phone_number": "+49 391 50963059",
    "top_reviews": [],
    "location": "",
    "questions_answers": [],
    "reviews_snippets": [
      {
        "reviewer_name": "https://www.google.com/maps/contrib/108961773063735587472?hl=en-VN",
        "reviewer_image_url": "https://lh3.googleusercontent.com/a-/ALV-UjVo7V5Twm5jLaJ47pz0paInjhqhRpvUOZ97kAAlXTLlv2VHa53B=w36-h36-p-k-rp-mo",
        "content": "\"Highly recommended place , very good taste , and very good staff and service.\""
      },
      {
        "reviewer_name": "https://www.google.com/maps/contrib/113571246890281614722?hl=en-VN",
        "reviewer_image_url": "https://lh3.googleusercontent.com/a-/ALV-UjVAnAibgPk1cbS-806rbxGoFNtutcgEr-Kib7a9s4_KA6Xi4nQ8=w36-h36-p-k-rp-mo",
        "content": "\"Delicious pizza with fresh juicy ingredients and crispy corners.\""
      }
    ],
    "photos_videos": [
      {
        "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNqyuLQX-a7b55F6gwFqYDnDJ81JvvIpFTAXjzF=w397-h298-k-no",
        "name": "All"
      },
      {
        "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSzZRfjhY2k-P0jZpNrHTIKLQZKT0TwxjWXADaOv712t4OZXXOEJpRh4cJn0A21eulO3W5TDkd3n5tuKrJllp-Xyce0Tf65LFEnR0YFPXViG0uUCvPCC-7_SPgkGpQ3dpeXL42dA8Q=w397-h298-k-no",
        "name": "Menu"
      },
      {
        "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNrG_ognGZwItd13OpjQ0PGZ8k4G9P-rAn6jz36=w224-h298-k-no",
        "name": "Food & drink"
      },
      {
        "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMbDiLVTeofcdf3Km0dbdwaBmlDsj6-IBHWcO6r=w397-h298-k-no",
        "name": "Vibe"
      },
      {
        "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSxc7ck75p3SI4eQsxs6GYTZOJmjvm_8TrSWIlbhdnH_OTHmpy9w6BB2wSsrPwsBOgucfMYMBfn-O-qpJzzcygowEP7A-lQs2OjqbeO8Bi7iwLfkDD9L7kePAoGOf8locDODeLdtFg=w224-h298-k-no",
        "name": "Pizza"
      },
      {
        "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOmIPvjskB5mIwniH8DzcssaKybKiAlEJsplKG9=w666-h298-k-no",
        "name": "By owner"
      },
      {
        "thumbnail": "https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=2m2SCHIzR1nR4g_sJmsc7Q&cb_client=maps_sv.tactile.gps&w=224&h=298&yaw=254.79843&pitch=0&thumbfov=100",
        "name": "Street View & 360°"
      }
    ],
    "people_also_search": [],
    "cid_location": "",
    "success": true,
    "error": "",
    "error_code": "",
    "err_stats": true,
    "input": {
      "url": "https://www.google.com/maps/place/Pizza%2BInn%2BMagdeburg/data=!4m7!3m6!1s0x47a5f50c083530a3:0xfdba8746b538141!8m2!3d52.1263086!4d11.6094743!16s%2Fg%2F11kqmtk3dt!19sChIJozA1CAz1pUcRQYFTa3So2w8?authuser=0%26hl=en%26rclk=1"
    }
  }
]
```

## 🚀 Quick Start

### 1. Get Credentials
Get your **free** scraping token from the [Thordata Dashboard](https://www.thordata.com/).

### 2. Install
```bash
git clone https://github.com/Thordata/google-maps-scraper-python.git
cd google-maps-scraper-python
pip install -r requirements.txt
```

### 3. Configure
Copy `.env.example` to `.env` and fill in your tokens:
```ini
THORDATA_SCRAPER_TOKEN=your_token_here
THORDATA_PUBLIC_TOKEN=your_public_token
THORDATA_PUBLIC_KEY=your_public_key
```

### 4. Run Scraper

**Search for businesses:**
```bash
python main.py search "Pizza in New York" --limit 10
```

**Get details (Deep Scrape):**
```bash
python main.py details 'https://www.google.com/maps/place/...'
```

**Get reviews:**
```bash
python main.py reviews 'https://www.google.com/maps/place/...' --limit 50
```

---

## 🏗️ Architecture

This scraper uses a **Hybrid Architecture** to ensure speed and cost-efficiency:

1.  **Search Phase**: Uses Thordata's **SERP API** for extremely fast retrieval of business lists.
2.  **Detail/Review Phase**: Uses Thordata's **Web Scraper API (Async Tasks)** to render full pages and extract deep attributes without getting blocked.

The `ThordataClient` automatically handles authentication, task polling, and error retries.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with ❤️ by the Thordata Developer Team.</sub>
</div>