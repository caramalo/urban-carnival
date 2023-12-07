import math

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from numpy.random import randint
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Set up Chrome webdriver (make sure to provide the path to your chromedriver.exe)
    chrome_path = "C:/Windows/chromedriver.exe"
    driver = webdriver.Chrome()

    title = input("Enter job title (ex: data scientist): ")
    location = input("Enter your zipcode or 'remote': ")

    if location.lower() == 'remote':
        distance = 'remote'
    else:
        distance = get_distance()

    salary = get_min_salary()

    # Build the Indeed search URL
    search_url = 'https://www.indeed.com/jobs?q={}&l={}&radius={}&minSalary={}&filter=0&sort=date&start={}'
    driver.get(search_url.format(title, location, distance, salary, 0))
    print("Search URL:", search_url.format(title, location, distance, salary, 0))
    job_count = driver.find_element(By.CLASS_NAME, 'jobsearch-JobCountAndSortPane-jobCount').text
    print("Job Count:", job_count)
    # Max number of pages for this search
    max_pages = math.ceil(int(job_count.split(' ')[0]) / 15)
    print("Max Pages:", max_pages)
    job_list = []

    for i in range(0, max_pages):
        driver.get(search_url.format(title, location, distance, salary, i * 10))

        try:

            # Use WebDriverWait to wait for the job results to be present
            job_page = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "mosaic-jobResults"))
            )
            jobs = job_page.find_elements(By.CLASS_NAME, "job_seen_beacon")

            for job in jobs:
                try:
                    job_title = job.find_element(By.CLASS_NAME, "jobTitle")
                    # company_name = job.find_element(By.CLASS_NAME, "companyName").text
                    # company_location = job.find_element(By.CLASS_NAME, "companyLocation").text
                    date = job.find_element(By.CLASS_NAME, "date").text
                    #salary_snippet = job.find_element(By.CLASS_NAME, "salary-snippet-container").text

                    job_list.append([job_title.text, job_title.find_element(By.CSS_SELECTOR, "a").get_attribute("href"),
                                    date])

                except NoSuchElementException as e:
                    print(f"Error extracting job details: {e}")

        except NoSuchElementException as e:
            print(f"Error finding job page: {e}")

    print(job_list[0:2])


def get_distance():
    while True:
        distance_input = input("Enter a distance in miles (5, 10, 15, 25, 35, 50, 100): ")
        if distance_input.isdigit() and int(distance_input) in [5, 10, 15, 25, 35, 50, 100]:
            return int(distance_input)
        else:
            print("Invalid input. Please enter a valid distance.")


def get_min_salary():
    while True:
        salary_input = input("Enter the minimum salary you are looking for without comma: ")
        if salary_input.isdigit():
            return int(salary_input)
        else:
            print("Invalid input. Please enter a valid salary.")


main()
