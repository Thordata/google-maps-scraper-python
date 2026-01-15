# main.py
import os
import json
import argparse
from dotenv import load_dotenv
from src.scraper import GoogleMapsScraper

load_dotenv()

def save_output(data, prefix):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{prefix}_results.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💾 Saved to: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Google Maps Scraper (Hybrid Mode)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search (SERP)
    search = subparsers.add_parser("search", help="Search via SERP API")
    search.add_argument("keyword", help="Search query (e.g. 'Pizza in NYC')")
    search.add_argument("--limit", type=int, default=20)

    # Details (Task)
    details = subparsers.add_parser("details", help="Deep scrape details via Task")
    details.add_argument("url", help="Google Maps Place URL")

    # Reviews (Task)
    reviews = subparsers.add_parser("reviews", help="Scrape reviews via Task")
    reviews.add_argument("url", help="Google Maps Place URL")
    reviews.add_argument("--days", type=int, default=0, help="Days limit (e.g. 30)")

    args = parser.parse_args()
    scraper = GoogleMapsScraper()

    if args.command == "search":
        data = scraper.search_businesses(args.keyword, args.limit)
        save_output(data, "search")

    elif args.command == "details":
        data = scraper.get_details(args.url)
        save_output(data, "details")

    elif args.command == "reviews":
        data = scraper.get_reviews(args.url, days_limit=args.days)
        save_output(data, "reviews")

if __name__ == "__main__":
    main()