# TrendPulse - Python Data Collection, Processing, Analysis and Visualization

## Project Overview

TrendPulse is a Python-based data analysis project that demonstrates a complete data workflow using live data from the Hacker News public API.

The project covers four main stages:

1. Data Collection
2. Data Processing
3. Data Analysis
4. Data Visualization

The collected data is processed and analyzed to identify important trends, keywords and highly scored stories.

## Objectives

- Collect live data using a public API.
- Clean and process the collected data.
- Perform statistical and descriptive analysis.
- Identify trending keywords and top stories.
- Create meaningful visualizations.
- Demonstrate a complete Python data analysis workflow.

## Tasks

### Task 1 - Data Collection

File: `task1_data_collection.py`

- Fetches the current top stories from the Hacker News API.
- Collects the top 50 stories.
- Extracts information such as:
  - Story ID
  - Title
  - Score
  - URL
  - Time
  - Author
  - Number of comments
- Adds the UTC collection timestamp.
- Saves the raw data for further processing.

### Task 2 - Data Processing

File: `task2_data_processing.py`

- Loads the collected raw data.
- Cleans and prepares the dataset.
- Handles missing or invalid values.
- Converts data into suitable formats.
- Saves the processed dataset for analysis.

### Task 3 - Data Analysis

File: `task3_data_analysis.py`

The analysis includes:

- Total number of stories
- Average score
- Median score
- Maximum score
- Total comments
- Trending keyword analysis
- Identification of important trends in the dataset

The analysis results are saved as:

- `analysis_summary.json`
- `top_keywords.csv`

### Task 4 - Data Visualization

File: `task4_visualization.py`

Creates visual representations of the analyzed data.

Generated visualizations:

- `top_keywords.png`
- `top_stories_by_score.png`

These graphs help understand trending keywords and highly scored stories.

## Technologies Used

- Python
- Requests
- Pandas
- Matplotlib
- JSON
- Hacker News Public API

## Project Structure

```text
TrendPulse/
│
├── README.md
├── requirements.txt
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_data_analysis.py
├── task4_visualization.py
│
├── analysis_summary.json
├── top_keywords.csv
├── top_keywords.png
└── top_stories_by_score.png
