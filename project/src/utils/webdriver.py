import time
import random  # Importing random module

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    """Create and configure a Chrome WebDriver instance in headless mode."""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')  # Disable GPU for headless mode (optional)
    
    # Set up ChromeDriver service and initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

def add_delay(min_delay=1, max_delay=3):
    """Introduce a delay between actions."""
    delay_time = random.uniform(min_delay, max_delay)  # Random delay
    time.sleep(delay_time)  # Introduce the delay
