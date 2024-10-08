def extract_basic_info(soup):
    try:
        name = soup.find('h1', class_='text-heading-xlarge').get_text(strip=True)
    except Exception as e:
        print(f"{e}")
        name = ''
    try:
        headline = soup.find('div', class_='text-body-medium').get_text(strip=True)
    except Exception as e:
        print(f"{e}")
        headline = ''
    try:
        e_div = soup.find('div', id='experience')
        e2_div = e_div.find_next_sibling('div')
        exp_div = e2_div.find_next_sibling('div')
        current_job_section = exp_div.find('li', class_=lambda c: 'artdeco-list__item' in c)
        job_title = current_job_section.find('span').get_text(strip=True)
    except Exception as e:
        print(f"{e}")
        job_title = ''
    try:
        e_div = soup.find('div', id='experience')
        e2_div = e_div.find_next_sibling('div')
        exp_div = e2_div.find_next_sibling('div')
        current_job_section = exp_div.find('li', class_=lambda c: 'artdeco-list__item' in c)
        company_name = current_job_section.find('span', class_='t-14')
        company_name = company_name.find('span', class_= 'visually-hidden').get_text(strip=True)
    except Exception as e:
        print(f"{e}")
        company_name = ''
    try:
        location_div = soup.find('div', class_ = 'mt2 relative')
        location_ul = location_div.find('ul')
        if location_ul is None:
            location_name = location_div.find('span', class_='text-body-small inline t-black--light break-words').get_text(strip=True)
        else:   
            location = location_ul.find_next_sibling('div')
            location_name = location.find('span', class_='text-body-small').get_text(strip=True)
    except Exception as e:
        print(f"{e}")
        location_name = ''
    try:
        connection_div = location_div.find_next_sibling('ul')
        conection_count = connection_div.find('span', class_="t-bold").get_text(strip = True)
    except Exception as e:
        print(f"{e}")
        connection_div = ''
    
    return [name, job_title, company_name, headline, location_name, conection_count]

def extract_about(soup):
    try:
        about_section = soup.find('div', {'id': 'about'})
        about_div = about_section.find_next_sibling('div')
        about_span = about_div.find_next_sibling('div')
        about_text = about_span.find('span',{'class':'visually-hidden'}).get_text(strip=True)
        return about_text
    except Exception as e:
        print(f"No about section found with error : {e}")
        return ""
