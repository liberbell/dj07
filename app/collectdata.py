from operator import imod
from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-beginner.herokuapp.com/udemy"

data1 = requests.get(URL)
# print(data1.status_code)
# print(data1.text)

soup = BeautifulSoup(data1.text, "html.parser")
# print(soup)
name= soup.select(".card-title")[0].string
print(name)

students = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers")[0].string
print(students)
students_split = students.split("：")
print(students_split)
print(students_split[1])

reviewer = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")[0].string
print(reviewer)