from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

# URL = "https://scraping-for-beginner.herokuapp.com/udemy"

# data1 = requests.get(URL)
# print(data1.status_code)
# print(data1.text)

# soup = BeautifulSoup(data1.text, "html.parser")
# print(soup)
# name= soup.select(".card-title")[0].string
# print(name)

# students = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers")[0].string
# print(students)
# students_split = students.split("：")
# students_num = int(students_split[1])
# print(students_num)

# reviewer = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")[0].string
# print(reviewer)
# reviewer_split = reviewer.split("：")
# reviewer_num = int(reviewer_split[1])
# print(reviewer_num)

# results ={
#     "name": name,
#     "students": students_num,
#     "reviewers": reviewer_num,
# }
# print(results)

df = pd.read_csv("assets/studentsnum.csv")
# print(df.head())

# print(datetime.datetime.today().strftime("%Y/%-m/%-d"))
# date = datetime.datetime.today().strftime("%Y/%-m/%-d")
# subscribers = results["students"]
# reviews = results["reviewers"]

# results = pd.DataFrame([[date, subscribers, reviews]], columns=["date", "subscribers", "reviews"])
# # print(results)
# df = pd.concat([df, results])
# # print(df.tail())

# df.to_csv("assets/data.csv", index=False)

def get_udemy_info():
    URL = "https://scraping-for-beginner.herokuapp.com/udemy"
    data1 = requests.get(URL)
    soup = BeautifulSoup(data1.text, "html.parser")

    name= soup.select(".card-title")[0].string

    students = soup.select(".subscribers")[0].string
    students_split = students.split("：")
    students_num = int(students_split[1])

    reviewer = soup.select(".reviews")[0].string
    reviewer_split = reviewer.split("：")
    reviewer_num = int(reviewer_split[1])

    results ={
    "name": name,
    "students": students_num,
    "reviewers": reviewer_num,
    }
    return results

def write_data():
    df = pd.read_csv("assets/studentsnum.csv")

    date = datetime.datetime.today().strftime("%Y/%-m/%-d")
    _results = get_udemy_info()
    subscribers = _results["students"]
    reviews = _results["reviewers"]
    results = pd.DataFrame([[date, subscribers, reviews]], columns=["date", "subscribers", "reviews"])

    df = pd.concat([df, results])
    df.to_csv("assets/data.csv", index=False)

df = pd.read_csv("assets/data.csv")
print(df.head())
print(df["date"][0])