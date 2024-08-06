from bs4 import BeautifulSoup
import time

def get_profile(driver, url, file_index):
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

    with open(f'/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data/profile_{file_index}.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    
    return soup