from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_connection_when_connect_is_available(driver, profile_url):
    connect_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//button[contains(@aria-label, 'Invite') and contains(@class, 'artdeco-button--primary') and contains(@class, 'pvs-profile-actions__action')]"))
    )
    connect_button.click()

    try:
        send_without_note_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[contains(@aria-label, 'Send without a note') and contains(@class, 'artdeco-button--primary')]"))
        )
        send_without_note_button.click()
        print(f"Connection request sent to {profile_url} without a note")
    except:
        send_now_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Send now')]"))
        )
        send_now_button.click()

        print(f"Connection request sent to {profile_url}")
        
def send_connection_from_more(driver, profile_url):

    more_actions_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ph5') and contains(@class, 'pb5')]//button[@aria-label='More actions']"))
    )
    more_actions_button.click()
    print("Clicked on the 'More actions' button.")

    dropdown_content = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ph5') and contains(@class, 'pb5')]//div[contains(@class, 'artdeco-dropdown__content-inner')]"))
    )
    print("Dropdown content is visible.")

    connect_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'ph5') and contains(@class, 'pb5')]//div[contains(@aria-label, 'Invite') and contains(@aria-label, 'to connect')]"))
    )
    connect_button.click()
    print("Clicked on the 'Connect' button.")
    try:
        send_without_note_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[contains(@aria-label, 'Send without a note') and contains(@class, 'artdeco-button--primary')]"))
        )
        send_without_note_button.click()
        print(f"Connection request sent to {profile_url} without a note")
    except:
        send_now_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Send now')]"))
        )
        send_now_button.click()

        print(f"Connection request sent to {profile_url}")

def send_connection_request(driver, profile_url):
    driver.get(profile_url)
    try:
        url = send_connection_when_connect_is_available(driver, profile_url)
        return profile_url
    except Exception as primary_error:
        print(f"Primary method failed. Trying alternative method. the error was {primary_error}")
    
        try:
            url = send_connection_from_more(driver, profile_url)
            return profile_url
        except Exception as secondary_error:
            print(f"Alternative method failed either you have already sent Connection request or something else went wrong the error :{secondary_error}")
            return None