import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


base_url = 'https://www.indeed.com'
start_path = '/jobs'
start_url = base_url + start_path

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

title = input("Enter job title (ex: data scientist): ")
location = input("Enter your zipcode or 'remote': ")

if location.lower() == 'remote':
    distance = 'remote'
else:
    distance = get_distance()

salary = get_min_salary()

# Build the Indeed search URL
search_params = f'?q={title.replace(" ", "+")}&l={location.replace(" ", "+")}&radius={distance}&minSalary={salary}'
search_url = base_url + start_path + search_params

# Add headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fetch the HTML content of the search results page with headers
response = requests.get(search_url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract job listings
    job_listings = soup.select(".jobsearch-SerpJobCard")

    for job_listing in job_listings:
        # Extract job details for each listing
        job_title = job_listing.select_one(".title a").get_text(strip=True)
        company_name = job_listing.select_one(".company span").get_text(strip=True)
        location = job_listing.select_one(".location span").get_text(strip=True)
        salary = job_listing.select_one(".salaryText").get_text(strip=True)
        job_type = job_listing.select_one(".jobType span").get_text(strip=True)

        # Output the results for each listing
        print("Job Title:", job_title)
        print("Company:", company_name)
        print("Location:", location)
        print("Salary:", salary)
        print("Job Type:", job_type)
        print("\n")  # Add a newline between listings

        # Add a delay between requests to avoid being blocked
        time.sleep(2)

    # Extract other job details as needed

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)