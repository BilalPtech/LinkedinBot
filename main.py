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
from app.utils.gsheet import write_to_google_sheet
import os

def main():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    message = "I HOPE YOU ARE DOING WELL AND THIS MESSAGE FINDS YOU IN GOOD HEALTH!"
    linkedin_login(driver=driver)
    job_title = 'AI Developer'
    num_of_ids_toget = 1
    profiles = search_job_title(driver=driver, job_title=job_title, idnums=num_of_ids_toget)
    print(profiles)
    for profile in profiles:
        url, sent_time = send_connection_request(driver, profile)
        if url is not None:
            insert_element(url)
        soup, soup_file = get_profile(driver=driver, url=profile)
        filename = f'{soup_file}.html'
        filepath = os.path.join('/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data', filename)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content, "html.parser")
            name, job_title, company_name, headline, location, con_count = extract_basic_info(soup)
            about = extract_about(soup)
            prof_info = {}
            prof_info["Name"] = name
            prof_info["URL"] = filename.replace('.html', '')
            prof_info["Job Title"] = job_title
            prof_info["Current Company"] = company_name
            prof_info["Headline"] = headline
            prof_info["Location"] = location
            prof_info["Connections Count"] = con_count
            prof_info["About"] = about
            prof_info["Connection Sent Time"] = sent_time
            write_to_google_sheet(prof_info)

    #send_messages_to_new_connects(driver, message)

    driver.quit()

if __name__ == '__main__':
    main()