# Amazon Review Scraper

A Python project that collects Amazon product reviews using Selenium, filters meaningful reviews, and performs basic text analysis and visualization.

This project demonstrates web scraping, data preprocessing, and simple natural language analysis on real-world e-commerce data.

---

## Features

- Automated Amazon review scraping
- Extraction of review metadata
- Filtering of verified and helpful reviews
- Word frequency analysis
- Word cloud visualization

---

## Tech Stack

Python  
Selenium  
Pandas  
Matplotlib  
WordCloud

---

## Project Structure

```
amazon-review-scraper
│
├── amazon_scraper.py
├── filter_reviews.py
├── word_frequency.py
├── word_cloud.py
├── README.md
```

---

## How It Works

### 1. Review Scraping

The scraper uses Selenium to navigate Amazon review pages and extract information including:

- rating
- review title
- review text
- review date
- verified purchase status
- helpful votes

Reviews are collected across multiple filters such as star ratings and sorting methods to maximize coverage.

---

### 2. Data Filtering

Collected reviews are filtered to keep only high-quality entries:

- verified purchases
- reviews with more than 10 helpful votes

This removes spam and low-quality reviews.

---

### 3. Text Analysis

The filtered review text is processed by:

- converting text to lowercase
- removing punctuation
- removing common stopwords

Word frequencies are then calculated to identify commonly mentioned topics.

---

### 4. Visualization

A word cloud is generated from the processed text to visually highlight the most frequent terms mentioned in reviews.

---

## Example Output

- CSV dataset of scraped reviews
- filtered review dataset
- word frequency results
- word cloud visualization

---

## Requirements

Install dependencies:

```
pip install selenium pandas matplotlib wordcloud
```

You also need:

- Microsoft Edge WebDriver
- Python 3.x

---

## Author

Imad Lembachar  
Computer Science Student