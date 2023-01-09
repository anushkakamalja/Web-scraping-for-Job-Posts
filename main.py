from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import time

today = date.today()
# print(today)

print("Enter some skills that you are unfamiliar with")
unfamiliar_skills= list(input(">").split(","))
print(f'Filtering out {",".join(unfamiliar_skills)}...')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
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
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {comp_name} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"Published Date: {date} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f'File saved: {index}.txt')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
