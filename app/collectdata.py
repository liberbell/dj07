from operator import imod
from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-beginner.herokuapp.com/udemy"

data1 = requests.get(URL)
# print(data1.status_code)
# print(data1.text)

soup = BeautifulSoup(data1.text, "html.parser")
# print(soup)
print(soup.select(".card-title")[0].string)