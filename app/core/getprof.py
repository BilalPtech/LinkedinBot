from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
import re

def sanitize_filename(url):

    parsed_url = urlparse(url)
    path = parsed_url.path
    
    match = re.search(r'/in/([^/?]+)', path)
    if match:
        filename = match.group(1)
    else:
        filename = path.strip('/').replace('/', '_')
    
    return filename

def get_profile(driver, url):
    driver.get(url)

    start = time.time()
    initialScroll = 0
    finalScroll = 1000
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll = finalScroll
        finalScroll += 1000
        time.sleep(5)
        end = time.time()
        if round(end - start) > 20:
            break

    soup = BeautifulSoup(driver.page_source, 'lxml')

    filename = sanitize_filename(url)

    with open(f'/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data/{filename}.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    
    return soup, filename