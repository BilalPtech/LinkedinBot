from app.utils.config import EMAIL, PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def linkedin_login(driver):
    driver.get('https://www.linkedin.com/login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    
    username_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search"]')))