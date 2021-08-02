from indeed import get_jobs as get_indeed_jobs
# scrapping?
# 다른 웹사이트에서 필요한 정보를 추출해옴
# - requests 모듈 https://docs.python-requests.org/en/master/ => html 가져옴
# - beautifulsoup 모듈 => html에서 원하는 정보만 추출

indeed_jobs = get_indeed_jobs()
print(indeed_jobs)
