"""Functions for extracting product data from Amazon pages."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_product_details(driver, product_element):
    """Extract details from a single product element."""
    try:
        details = {
            'name': _get_product_name(product_element),
            'price': _get_product_price(product_element),
            'discount': _get_discount(product_element),
            'rating': _get_rating(product_element),
            'ship_from': _get_shipping_info(product_element),
            'sold_by': _get_seller_info(product_element),
            'description': _get_description(product_element),
            'monthly_sales': _get_monthly_sales(product_element),
            'images': _get_product_images(product_element)
        }
        return details
    except Exception as e:
        print(f"Error extracting product details: {str(e)}")
        return None

def _get_product_name(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "span.a-text-normal").text
    except:
        return ""

def _get_product_price(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
    except:
        return ""

def _get_discount(element):
    try:
        discount_element = element.find_element(By.CSS_SELECTOR, "span.a-text-price")
        return discount_element.text
    except:
        return ""

def _get_rating(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "span.a-icon-alt").get_attribute("innerHTML")
    except:
        return ""

def _get_shipping_info(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "div.a-row.a-size-base.a-color-secondary").text
    except:
        return ""

def _get_seller_info(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "div.a-row.a-size-small").text
    except:
        return ""

def _get_description(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "div.a-row.a-size-base").text
    except:
        return ""

def _get_monthly_sales(element):
    try:
        return element.find_element(By.CSS_SELECTOR, "span.a-size-small.a-color-secondary").text
    except:
        return ""

def _get_product_images(element):
    try:
        images = element.find_elements(By.CSS_SELECTOR, "img.s-image")
        return [img.get_attribute("src") for img in images]
    except:
        return []