from bs4 import BeautifulSoup
import requests

url = 'http://reevepaul.pythonanywhere.com/'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
print( soup.a)