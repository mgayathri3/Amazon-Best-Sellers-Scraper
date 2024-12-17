"""Configuration settings for the Amazon scraper."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Amazon credentials
AMAZON_EMAIL = os.getenv('AMAZON_EMAIL')
AMAZON_PASSWORD = os.getenv('AMAZON_PASSWORD')

# URLs
BASE_URL = "https://www.amazon.in"
BESTSELLER_URL = f"{BASE_URL}/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2"

# Categories to scrape
CATEGORIES = [
    'kitchen',
    'shoes',
    'computers',
    'electronics',
    'books',
    'grocery',
    'beauty',
    'home_improvement',
    'toys',
    'sports'
]

# Scraping settings
MAX_PRODUCTS_PER_CATEGORY = 1500
MIN_DISCOUNT_PERCENTAGE = 50

# Selenium settings
IMPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30