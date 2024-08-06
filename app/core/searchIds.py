from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_job_title(driver, job_title, idnums):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search"]'))
        )
    except:
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.search-global-typeahead__collapsed-search-button'))
        )
        search_button.click()
        
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search"]'))
        )

    search_box.send_keys(job_title)
    search_box.send_keys(Keys.RETURN)
    
    
    people_tab = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "artdeco-pill--choice") and text()="People"]'))
    )
    people_tab.click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.reusable-search__result-container')))
    

    profile_links = driver.find_elements(By.CSS_SELECTOR, '.reusable-search__result-container .entity-result__title-text a')
    
    return [link.get_attribute('href') for link in profile_links[:idnums]]