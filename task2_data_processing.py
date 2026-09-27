"""
TrendPulse - Task 2: Data Processing
Cleans raw story data and creates a normalized dataset.
Run after task1_data_collection.py: python task2_data_processing.py
"""
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

def main():
    source = DATA_DIR / "raw_trends.csv"
    if not source.exists():
        raise FileNotFoundError("data/raw_trends.csv not found. Run Task 1 first.")

    df = pd.read_csv(source)
    initial_count = len(df)

    df = df.dropna(subset=["id", "title"]).copy()
    df["title"] = df["title"].astype(str).str.strip()
    df = df[df["title"] != ""]
    df = df.drop_duplicates(subset=["id"], keep="first")

    for column in ["score", "descendants", "time"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    df["score"] = df["score"].fillna(0).astype(int)
    df["descendants"] = df["descendants"].fillna(0).astype(int)
    df["published_at_utc"] = pd.to_datetime(
        df["time"], unit="s", utc=True, errors="coerce"
    ).astype("string")

    df["title_word_count"] = df["title"].str.split().str.len()
    output = DATA_DIR / "cleaned_trends.csv"
    df.to_csv(output, index=False)
    print(f"Rows before cleaning: {initial_count}")
    print(f"Rows after cleaning:  {len(df)}")
    print(f"Clean data saved -> {output}")

if __name__ == "__main__":
    main()
