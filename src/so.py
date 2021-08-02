from bs4 import BeautifulSoup
import requests

URL = 'https://stackoverflow.com/jobs?q=python'


def get_last_page():
   result = requests.get(URL)
   soup = BeautifulSoup(result.text, "html.parser")
   pagination = soup.find("div", {"class": "s-pagination"})
   links = pagination.find_all('a')
   pages=[]
   for link in links[0:-1]:
      pages.append(int(link.find('span').string))
   max_page = pages[-1]
   return max_page

def extract_job(html):
   title = html.find()


def extract_jobs(last_page):
   # for page in range(last_page):
      result = requests.get(f"https://stackoverflow.com/jobs?q=python&pg={1}")
      soup = BeautifulSoup(result.text, "html.parser")
      list_results = soup.find("div",{"class":"listResults"})
      list_result=list_results.find_all("div")
      for jobcard in list_result:
         job = extract_job(jobcard)
         print(job)


def get_jobs():
   last_page = get_last_page()
   jobs = extract_jobs(last_page)
   # return jobs

get_jobs()
