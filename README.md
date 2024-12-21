# Yahoo Finance Scraper

A lightweight Python-based scraper designed to extract financial data from Yahoo Finance's HTML tables and structure it for analysis.

## Features

- **Efficient Parsing**: Extracts financial data like `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, and `Volume`.
- **Data Output**: Displays data in a tabular format for easy analysis.

## Prerequisites

Ensure the following tools and libraries are installed:

- **Python**: Version 3.7 or higher.
- **Dependencies**: Install via `requirements.txt`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KaanRich/yahoo-finance-scraper.git
   cd yahoo-finance-scraper

# Usage
## Extract HTML Content:
   - Open the Yahoo Finance page.
   - Choose a stock and navigate to the **"Historical Data"** tab.
   - Select the desired date range for the financial data.
   - Right-click on the table element containing the financial data and choose **Inspect**.
   - In the browser's Developer Tools, locate the `<table>` element.
   - Right-click the `<table>` element and select **Copy > Copy outerHTML**.
   - Replace the `html_data` variable in `yfs.py` with the copied HTML content.

## Run the Script:

 ```bash
python yfs.py
 ```
    
# Example Output
Sample Table:
After running the script, you'll get a DataFrame structured like this:

Date	Open	High	Low	Close	Adj Close	Volume
| Date        | Open   | High   | Low    | Close  | Adj Close | Volume       |
|-------------|--------|--------|--------|--------|-----------|--------------|
...
| Dec 19, 2024 | 451.88 | 456.36 | 420.02 | 436.17 | 436.17    | 118,566,100  |
| Dec 20, 2024 | 425.51 | 447.08 | 417.64 | 421.06 | 421.06    | 131,374,800  |
...

# How It Works
- HTML Parsing: The script uses BeautifulSoup to extract table data from Yahoo Finance HTML.
- Data Processing: Processes rows to extract key metrics.
- Output Formatting: Structures data into a Pandas DataFrame.

# Disclaimer
This project is intended for educational purposes only. Make sure to comply with Yahoo Finance's Terms of Service when using this tool.
