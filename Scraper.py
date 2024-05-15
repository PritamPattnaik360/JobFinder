import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(title, location, times):
    id_list = []
    for t in range(times):
        list_url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={title}&location={location}&start={t}"

        response = requests.get(list_url)

        list_data = response.text
        list_soup = BeautifulSoup(list_data, "html.parser")
        page_jobs = list_soup.find_all("li")

        for job in page_jobs:
            base_card_div = job.find("div", {"class": "base-card"})
            job_id = base_card_div.get("data-entity-urn").split(":")[3]
            id_list.append(job_id)

    job_list = []

    for job_id in id_list:
        job_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
        
        job_response = requests.get(job_url)
        job_soup = BeautifulSoup(job_response.text, "html.parser")
        
        job_post = {}
        
        try:
            job_post["job_title"] = job_soup.find("h2", {"class":"top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"}).text.strip()
        except:
            job_post["job_title"] = None
        try:
            job_post["company_name"] = job_soup.find("a", {"class": "topcard__org-name-link topcard__flavor--black-link"}).text.strip()
        except:
            job_post["company_name"] = None
        try:
            job_post["time_posted"] = job_soup.find("span", {"class": "posted-time-ago__text topcard__flavor--metadata"}).text.strip()
        except:
            job_post["time_posted"] = None
        try:
            job_post["num_applicants"] = job_soup.find("span", {"class": "num-applicants__caption topcard__flavor--metadata topcard__flavor--bullet"}).text.strip()
        except:
            job_post["num_applicants"] = None
        try:
            job_post["app_link"] = job_soup.find("a", {"class": "topcard__link"})["href"]
        except:
            job_post["app_link"] = None

        job_list.append(job_post)

    jobs_df = pd.DataFrame(job_list)
    jobs_df.to_csv('Data.csv', index=False)

if __name__ == "__main__":#testing purposes
    title = "Software Developer"  # Job title
    location = "New Jersey"  # Job location
    scrape(title, location, 2)
    print('finished')
