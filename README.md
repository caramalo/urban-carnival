# urban-carnival
 A job aggregator via scraping data from indeed using selenium.
 
# Indeed Web Scraper

## Introduction

The Indeed Web Scraper is a Python script that uses Selenium to scrape job listings from Indeed. It allows you to input a job title, location, and minimum salary to fetch job details such as job title, company name, location, salary, date, and a link to the job posting.

## Prerequisites

Before running the script, make sure you have the following installed:

- **Python (3.x recommended):** [Download Python](https://www.python.org/downloads/)
- **ChromeDriver:** [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Setup

1. **Install Dependencies**

   Open a terminal and navigate to the project directory. Run the following command to install the required Python packages:

   ```bash
   pip install selenium pandas openpyxl
2. **Configure ChromeDriver Path**

   Update the chrome_path variable in the script to the path where you have downloaded chromedriver.exe. For example:
   ```bash
   chrome_path = "C:/path/to/chromedriver.exe"

## Usage

1. Run the script:

   ```bash
   python your_script_name.py
2. Input the job title, location, and other details as prompted.

3. Wait for the script to scrape job listings.

4. Once completed, the script will generate an Excel file (output_jobs.xlsx) containing the scraped data.

## Notes
Ensure that your internet connection is stable during execution.
Make sure the chromedriver.exe path is correctly set.
Adjust the script as needed for specific job search requirements.
