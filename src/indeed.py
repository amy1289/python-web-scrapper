from bs4 import BeautifulSoup
# scrapping?
# 다른 웹사이트에서 필요한 정보를 추출해옴
# - requests 모듈 https://docs.python-requests.org/en/master/ => html 가져옴
# - beautifulsoup 모듈 => html에서 원하는 정보만 추출
import requests

URL = 'https://kr.indeed.com/jobs?q=python&l=서울'


def get_last_page():
   result = requests.get(URL)

   soup = BeautifulSoup(result.text, "html.parser")

   pagination = soup.find("div", {"class": "pagination"})
   links = pagination.find_all('a')

   pages = []
   for link in links[0:-1]:  # 0 ~ 끝에서 첫번째꺼 제외하고
      pages.append(int(link.find('span', {'class': 'pn'}).string))
      #pages.append(int(link.string))

   max_page = pages[-1]  # 마지막 페이지
   # print(max_page)
   return max_page

def extract_job(html):
   title = html.find('a', {'class': 'jobtitle'})["title"]
   company = html.find('span', {'class': 'company'}).text.replace("\n", "")
   job_id = html["data-jk"]
   return {"title": title, "company": company, "link": f"https://kr.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page):
   jobs = []
   for page in range(last_page):  # pages는 2~5인데(1없고 max_page까지) range는 0~4로 배열(max_page length의 0~max_page-1 배열)만들어줌
      result=requests.get(f"{URL}&start={page*10}")
      soup = BeautifulSoup(result.text, "html.parser")
      jobcards = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
      for jobcard in jobcards[0:len(jobcards)-1]: 
         job = extract_job(jobcard)
         jobs.append(job)
   return jobs

def get_jobs():
   last_page = get_last_page()
   # 1 ~ 마지막 페이지 까지 request 보내기
   jobs = extract_jobs(last_page)
   return jobs
