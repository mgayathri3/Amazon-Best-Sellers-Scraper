import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from utils.webdriver import create_driver, add_delay
from utils.auth import login
from utils.data_extractor import extract_product_details
from utils.data_storage import save_to_json, save_to_csv
from config import (
    AMAZON_EMAIL, AMAZON_PASSWORD, BESTSELLER_URL, CATEGORIES,
    MAX_PRODUCTS_PER_CATEGORY, MIN_DISCOUNT_PERCENTAGE
)

class AmazonBestSellerScraper:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        """Initialize the web driver and login."""
        self.driver = create_driver()  # Initialize the WebDriver
        if not login(self.driver, AMAZON_EMAIL, AMAZON_PASSWORD):
            raise Exception("Failed to login to Amazon")
    
    def scrape_category(self, category):
        """Scrape products from a specific category."""
        url = f"https://www.amazon.in/gp/bestsellers/{category}"
        self.driver.get(url)
        
        products = []
        page = 1
        
        while len(products) < MAX_PRODUCTS_PER_CATEGORY:
            try:
                # Wait for products to load
                product_elements = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.a-section.a-spacing-none"))
                )
                
                for element in product_elements:
                    product_data = extract_product_details(self.driver, element)
                    if product_data and self._meets_criteria(product_data):
                        products.append(product_data)
                
                # Try to go to next page
                if not self._go_to_next_page():
                    break
                    
                page += 1
                add_delay()  # Add delay between pages to avoid detection
                
            except TimeoutException:
                print(f"Timeout while scraping category: {category}")
                break
            except Exception as e:
                print(f"Error scraping category {category}: {str(e)}")
                break
        
        return products
    
    def scrape_all_categories(self):
        """Scrape all specified categories."""
        all_data = {}
        
        for category in CATEGORIES:
            print(f"Scraping category: {category}")
            products = self.scrape_category(category)
            all_data[category] = products
            
            # Save data for each category
            save_to_json(products, category)
            save_to_csv(products, category)
            
            # Small delay between categories
            add_delay(2, 4)  # Custom delay between categories
        
        return all_data
    
    def _meets_criteria(self, product_data):
        """Check if product meets the scraping criteria."""
        try:
            discount = float(product_data['discount'].replace('%', ''))
            return discount >= MIN_DISCOUNT_PERCENTAGE
        except:
            return False
    
    def _go_to_next_page(self):
        """Attempt to navigate to the next page."""
        try:
            next_button = self.driver.find_element(By.CSS_SELECTOR, "li.a-last a")
            next_button.click()
            add_delay()  # Delay after clicking the next button
            return True
        except NoSuchElementException:
            return False
    
    def cleanup(self):
        """Clean up resources."""
        if self.driver:
            self.driver.quit()
