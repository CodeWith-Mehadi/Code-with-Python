import requests
from bs4 import BeautifulSoup

url = "https://iubat.edu/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.body.text)