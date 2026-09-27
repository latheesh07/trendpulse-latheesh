"""
TrendPulse - Task 4: Data Visualization
Creates PNG charts from the processed and analyzed data.
Run after task3_data_analysis.py: python task4_visualization.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    clean_path = DATA_DIR / "cleaned_trends.csv"
    keywords_path = OUTPUT_DIR / "top_keywords.csv"
    if not clean_path.exists() or not keywords_path.exists():
        raise FileNotFoundError("Run Tasks 1, 2 and 3 before Task 4.")

    stories = pd.read_csv(clean_path)
    keywords = pd.read_csv(keywords_path)

    if not keywords.empty:
        plot_data = keywords.head(10).sort_values("frequency")
        plt.figure(figsize=(10, 6))
        plt.barh(plot_data["keyword"], plot_data["frequency"])
        plt.title("Most Frequent Words in Top Story Titles")
        plt.xlabel("Frequency in titles")
        plt.ylabel("Keyword")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "top_keywords.png", dpi=200)
        plt.close()

    top_stories = stories.nlargest(10, "score").sort_values("score")
    plt.figure(figsize=(11, 7))
    plt.barh(top_stories["title"], top_stories["score"])
    plt.title("Top 10 Hacker News Stories by Score")
    plt.xlabel("Story score")
    plt.ylabel("Story title")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_stories_by_score.png", dpi=200)
    plt.close()

    print(f"Charts saved in: {OUTPUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
