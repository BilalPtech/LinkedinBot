from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from urllib.parse import urlparse, urlunparse
import os

def strip_url(url):
    parsed_url = urlparse(url)
    return urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))

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
    
    fetched_profiles = []

    if os.path.getsize('/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data/cache.json') > 0:
        with open('/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data/cache.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if isinstance(data, list):
            cache = data
            for link in profile_links:
                href = link.get_attribute('href')
                stripped_href = strip_url(href)
                if stripped_href not in cache:
                    fetched_profiles.append(stripped_href)
                    if len(fetched_profiles) >= idnums:
                        break
        
            return fetched_profiles
        else:
            print("JSON data is not list")
            return [strip_url(link.get_attribute('href')) for link in profile_links[:idnums]]
    else:
        print("JSON data is empty")
        return [strip_url(link.get_attribute('href')) for link in profile_links[:idnums]]