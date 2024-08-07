from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.utils.cache import delete_element
import time
import json

def send_messages_to_new_connects(driver, message):
    new_links = get_your_connections(driver)
    with open('/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data/cache.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if isinstance(data, list):
        cache = data
    else:
        raise ValueError("JSON data is not a list")
    
    temp_list = []
    updated_cache = [link for link in cache if not (link in new_links and temp_list.append(link) or True)]
    for link in temp_list:
        print(link)
        send_message(driver, link, message)
        delete_element(link)

def get_your_connections(driver):
    connections_url = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'
    driver.get(connections_url)
    time.sleep(5)

    profile_links = set()
    connections = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/in/"]')
    for connection in connections:
        href = connection.get_attribute("href")
        profile_links.add(strip_trailing_slash(href))
    
    return profile_links

def send_message(driver, profile_url, message):
 
    driver.get(profile_url)

    message_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'artdeco-button--primary') and contains(@class, 'pvs-profile-actions__action') and span[text()='Message']]"))
    )
    message_button.click()
    
    message_textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='textbox']"))
    )
    message_textarea.click()
    message_textarea.send_keys(message)
    
    try:
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'msg-form__send-button') and contains(@class, 'artdeco-button--1')]"))
        )
    except:
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'msg-form__send-btn') and contains(@class, 'artdeco-button--1')]"))
        )
    send_button.click()

    time.sleep(5)

def strip_trailing_slash(url):
    if url.endswith('/'):
        return url[:-1]
    return url