from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta

today = date.today()
# print(today)

print("Enter some skills that you are unfamiliar with")
unfamiliar_skills= list(input(">").split(","))
print(f'Filtering out {unfamiliar_skills}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if published_date[7].isnumeric() :
        date = today - timedelta(days= int(published_date[7]))
        comp_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('span', class_ = 'srp-skills').text
        # print(skills)
        more_info = job.header.h2.a['href']
        unfamiliar_skill_detected = False
        for unfamiliar_skill in unfamiliar_skills:
            if unfamiliar_skill.lower() in skills.lower():
                unfamiliar_skill_detected = True
             
        if unfamiliar_skill_detected is False:
            print(f"Company Name: {comp_name}")
            print(f"Required Skills: {skills.strip()}")
            print(f"Published Date: {date}")
            print(f"More Info: {more_info}")
            print('')    
