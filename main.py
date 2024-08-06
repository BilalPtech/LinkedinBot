from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.core.login import linkedin_login
from app.core.searchIds import search_job_title
from app.core.sendReq import send_connection_request
from app.utils.cache import insert_element
from app.core.getprof import get_profile
from app.core.sendMsg import send_messages_to_new_connects
from app.core.scrapProf import extract_about, extract_basic_info
from bs4 import BeautifulSoup
import os

def main():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    message = "I HOPE YOU ARE DOING WELL AND THIS MESSAGE FINDS YOU IN GOOD HEALTH!"
    linkedin_login(driver=driver)
    job_title = 'Data analyst'
    num_of_ids_toget = 1
    profiles = search_job_title(driver=driver, job_title=job_title, idnums=num_of_ids_toget)
    for index, profile in enumerate(profiles):
        url = send_connection_request(driver, profile)
        if url is not None:
            insert_element(url)
        soup = get_profile(driver=driver, url=profile, file_index=index)
    send_messages_to_new_connects(driver, message)

    driver.quit()

    for filename in os.listdir('/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data'):
        if filename.endswith(".html"):
            filepath = os.path.join('/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data', filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                soup = BeautifulSoup(content, "html.parser")
                name, job_title, company_name, headline, location, con_count = extract_basic_info(soup)
                about = extract_about(soup)
                print(f"Name: {name}")
                print(f"Job Title: {job_title}")
                print(f"Current Company: {company_name}")
                print(f"Headline: {headline}")
                print(f"Location: {location}")
                print(f"Connections Count: {con_count}")
                print(f'About: {about}')

if __name__ == '__main__':
    main()