from bs4 import BeautifulSoup
import requests
from bs4 import Tag
from typing import cast 
import os
import time
# cast cant handle None 



# content: my link or content of site
# soup=BeautifulSoup(content,'lxml') instance of my library
# soup.find_all()
# request lib requests info from any website


# web_page=requests.get('https://internshala.com/internships/keywords-Mumbai/')
# print(web_page) gives output 200 that tells me that the request of was successfully recieved
print("Looking for 'jobs' Or 'Internship'?")
role=input(">>>").lower()
role_link="https://internshala.com/"+role+"/"
web_page=requests.get(role_link).text
# print(web_page)
soup=BeautifulSoup(web_page,'lxml')
city=input(f"What city/state do wish to find a {role} in?\n>>>").lower()
print("Searching...")


def finding_role():
    jobs = soup.find_all('div', class_='internship_meta experience_meta')

    for index,job in enumerate(jobs):
        job = cast(Tag, job)

        time_div = job.find('div', class_="color-labels")
        has_time_span = time_div and time_div.span
        time_detail = time_div.span.text.strip() if has_time_span else ""



        if "Few" in time_detail or "Today" in time_detail:
            
            
            location_tag = job.find('p', class_="row-1-item locations")
            has_location = location_tag and location_tag.span and location_tag.span.a
            location_det = location_tag.span.a.text.strip() if has_location else "N/A"
            loc=(location_det).lower()
            if city in loc:

                company_tag = job.find('p', class_="company-name")
                has_company = company_tag is not None
                company_name = company_tag.text.strip() if has_company else "N/A"

                h3_tag = job.find('h3', class_="job-internship-name")
                has_h3 = h3_tag and h3_tag.a
                post_title = h3_tag.a.text.strip() if has_h3 else "N/A"
                link_info = h3_tag.a['href'] if has_h3 and h3_tag.a.has_attr('href') else ""


                safe_name = company_name.replace("/", "_").replace("\\", "_")
                with open(f"posts/{safe_name}.txt","w") as file:
                    file.write(f"Company: {company_name}\n")
                    file.write(f"Located at: {location_det}\n")
                    file.write(f"Posted: {time_detail}\n")
                    file.write(f"Post: {post_title}\n")
                    file.write(f"More Info: https://internshala.com{link_info}\n\n\n")
                print(f"Found {company_name}..")
    print("Saved all found matches")

if __name__ == '__main__':
    while True:
        finding_role()
        time_wait_mins=5
        print(f"Waiting for next search in {time_wait_mins} minutes..")
        # time.sleep(time_wait_mins*60)
        time.sleep(6)