import json
import os
from pathlib import Path

from dotenv import load_dotenv

from src.scraper import GoogleMapsScraper


def main() -> None:
    """
    Trigger all Google Maps spiders using the same parameters as in the
    official documentation. This is intended for end-to-end regression
    testing with real token consumption.
    """
    load_dotenv()

    scraper = GoogleMapsScraper()

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)

    def _save(name: str, data) -> None:
        path = out_dir / f"{name}.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {path}")

    # 1) google_map-details_by-url
    details_by_url_data = scraper.details_by_url(
        {
            "url": "https://www.google.com/maps/place/"
            "Pizza%2BInn%2BMagdeburg/data=!4m7!3m6!1s0x47a5f50c083530a3:"
            "0xfdba8746b538141!8m2!3d52.1263086!4d11.6094743!16s%2Fg%2F11kqmtk3dt!"
            "19sChIJozA1CAz1pUcRQYFTa3So2w8?authuser=0%26hl=en%26rclk=1"
        }
    )
    _save("details_by_url", details_by_url_data)

    # 2) google_map-details_by-cid
    details_by_cid_data = scraper.details_by_cid({"CID": "2476046430038551731"})
    _save("details_by_cid", details_by_cid_data)

    # 3) google_map-details_by-location
    details_by_location_data = scraper.details_by_location(
        {
            "country": "United States",
            "keyword": "pizza",
            "lat": "33",
            "long": "118",
            "zoom_level": "25",
        }
    )
    _save("details_by_location", details_by_location_data)

    # 4) google_map-details_by-placeid
    details_by_placeid_data = scraper.details_by_placeid(
        [
            {"place_id": "ChIJ3S-JXmauEmsRUcIaWtf4MzE"},
            {"place_id": "ChIJLU7jZClu5kcR4PcOOO6p3I0"},
            {"place_id": "ChIJPTacEpBQwokRKwIlDXelxkA"},
        ]
    )
    _save("details_by_placeid", details_by_placeid_data)

    # 5) google_comment_by-url
    reviews_by_url_data = scraper.reviews_by_url(
        [
            {
                "url": (
                    "https://www.google.com/maps/place/Waterfront%2BBotanical%2BGardens/"
                    "@38.2630366,-85.7288454,15z/data=!4m8!3m7!1s0x8869731e16a7bdbd:"
                    "0x2f5d238fefed7ca1!8m2!3d38.2632837!4d-85.7239738!9m1!1b1!"
                    "16s%2Fg%2F11c709xzzx?hl=en%26entry=ttu"
                ),
                "days_limit": "10",
            },
            {
                "url": (
                    "https://www.google.com/maps/place/Crash%2BChampions%2BCollision%2B"
                    "Repair%2BSouthwest%2BFreeway/@29.6665614,-95.5500391,17z/data=!4m8!"
                    "3m7!1s0x8640e81b678a64ab:0xe6412a1e06fae48!8m2!3d29.6665614!"
                    "4d-95.5500391!9m1!1b1!16s%2Fg%2F1txy2r0t?hl=en%26entry=ttu"
                ),
                "days_limit": "10",
            },
        ]
    )
    _save("reviews_by_url", reviews_by_url_data)


if __name__ == "__main__":
    main()

