from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta

today = date.today()
# print(today)
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if published_date[7].isnumeric() :
        date = today - timedelta(days= int(published_date[7]))
        comp_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('span', class_ = 'srp-skills').text.strip()
        
        print(f'''
        Company Name: {comp_name}
        Required Skills: {skills}
        Published Date: {date}
        ''')
        print('')
