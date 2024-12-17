# Amazon Best Sellers Scraper

A Python-based web scraper for extracting product information from Amazon's Best Sellers section.

## Features

- Authenticates with Amazon credentials
- Scrapes product details from 10 different categories
- Focuses on products with >50% discount
- Extracts comprehensive product information
- Saves data in both JSON and CSV formats
- Implements robust error handling
- Follows modular and maintainable code structure

## Prerequisites

- Python 3.8+
- Chrome browser installed

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your Amazon credentials:
   ```bash
   cp .env.example .env
   ```

## Project Structure

```
├── src/
│   ├── config.py           # Configuration settings
│   ├── scraper.py         # Main scraper implementation
│   └── utils/
│       ├── auth.py        # Authentication utilities
│       ├── data_extractor.py  # Data extraction functions
│       ├── data_storage.py    # Data storage utilities
│       └── webdriver.py       # WebDriver management
├── data/                  # Scraped data storage
├── main.py               # Entry point
├── requirements.txt      # Project dependencies
└── README.md            # Documentation
```

## Usage

1. Ensure your Amazon credentials are set in the `.env` file
2. Run the scraper:
   ```bash
   python main.py
   ```

The scraped data will be saved in the `data` directory in both JSON and CSV formats.

## Data Collected

For each product:
- Product Name
- Product Price
- Sale Discount
- Best Seller Rating
- Ship From
- Sold By
- Rating
- Product Description
- Number Bought in Past Month
- Category Name
- Available Images

## Error Handling

The scraper includes:
- Retry mechanism for login
- Timeout handling
- Exception catching and logging
- Graceful cleanup of resources

## Compliance

This scraper is designed to respect Amazon's terms of service by:
- Including appropriate delays between requests
- Using reasonable rate limits
- Properly identifying itself through user-agent
- Not overloading servers