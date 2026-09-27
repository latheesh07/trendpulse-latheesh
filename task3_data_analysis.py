"""
TrendPulse - Task 3: Data Analysis
Summarizes cleaned stories and extracts frequent title keywords.
Run after task2_data_processing.py: python task3_data_analysis.py
"""
from pathlib import Path
from collections import Counter
import re
import json
import pandas as pd

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

STOPWORDS = {
    "the", "and", "for", "with", "from", "this", "that", "are", "you",
    "your", "how", "what", "why", "new", "has", "have", "was", "will",
    "into", "about", "after", "over", "under", "its", "their", "they",
    "but", "not", "can", "all", "one", "out", "use", "using"
}

def main():
    source = DATA_DIR / "cleaned_trends.csv"
    if not source.exists():
        raise FileNotFoundError("data/cleaned_trends.csv not found. Run Task 2 first.")

    df = pd.read_csv(source)
    if df.empty:
        raise ValueError("The cleaned dataset is empty.")

    tokens = []
    for title in df["title"].dropna().astype(str):
        for word in re.findall(r"[a-zA-Z]{3,}", title.lower()):
            if word not in STOPWORDS:
                tokens.append(word)

    keyword_counts = Counter(tokens)
    keywords = pd.DataFrame(
        keyword_counts.most_common(15), columns=["keyword", "frequency"]
    )
    keywords.to_csv(OUTPUT_DIR / "top_keywords.csv", index=False)

    top_story = df.sort_values("score", ascending=False).iloc[0]
    summary = {
        "total_stories": int(len(df)),
        "average_score": round(float(df["score"].mean()), 2),
        "median_score": float(df["score"].median()),
        "maximum_score": int(df["score"].max()),
        "total_comments_reported": int(df["descendants"].sum()),
        "highest_score_story_title": str(top_story["title"]),
        "highest_score_story_score": int(top_story["score"]),
        "keyword_method": "Frequency of words in story titles after basic stopword removal"
    }
    with open(OUTPUT_DIR / "analysis_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("Analysis summary:")
    for key, value in summary.items():
        print(f"- {key}: {value}")
    print(f"Keyword table saved -> {OUTPUT_DIR / 'top_keywords.csv'}")

if __name__ == "__main__":
    main()
