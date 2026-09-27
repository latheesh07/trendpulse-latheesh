"""
TrendPulse - Task 1: Data Collection
Fetches the current top stories from the public Hacker News API and saves raw data.
Run: python task1_data_collection.py
"""
from pathlib import Path
from datetime import datetime, timezone
import time
import requests
import pandas as pd

BASE_URL = "https://hacker-news.firebaseio.com/v0"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def main():
    response = requests.get(f"{BASE_URL}/topstories.json", timeout=20)
    response.raise_for_status()
    story_ids = response.json()[:50]

    records = []
    for story_id in story_ids:
        try:
            item_response = requests.get(
                f"{BASE_URL}/item/{story_id}.json", timeout=20
            )
            item_response.raise_for_status()
            item = item_response.json()
            if not item or item.get("type") != "story":
                continue
            records.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "score": item.get("score"),
                "url": item.get("url"),
                "time": item.get("time"),
                "by": item.get("by"),
                "descendants": item.get("descendants", 0),
                "collected_at_utc": datetime.now(timezone.utc).isoformat()
            })
            time.sleep(0.05)  # be considerate to the API
        except requests.RequestException as exc:
            print(f"Could not fetch story {story_id}: {exc}")

    if not records:
        raise RuntimeError("No stories were collected. Check your internet connection/API.")

    output = DATA_DIR / "raw_trends.csv"
    pd.DataFrame(records).to_csv(output, index=False)
    print(f"Collected {len(records)} stories -> {output}")

if __name__ == "__main__":
    main()
