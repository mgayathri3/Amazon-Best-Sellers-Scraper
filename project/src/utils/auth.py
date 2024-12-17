"""Authentication utilities for Amazon login."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from retry import retry

@retry(tries=3, delay=2)
def login(driver, email, password):
    """Login to Amazon using provided credentials."""
    try:
        # Navigate to sign-in page
        driver.get("https://www.amazon.in/ap/signin")
        
        # Enter email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_field.send_keys(email)
        driver.find_element(By.ID, "continue").click()
        
        # Enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_field.send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()
        
        return True
    except Exception as e:
        print(f"Login failed: {str(e)}")
        return False