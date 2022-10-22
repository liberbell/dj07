from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

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

if __name__ == "__main__":
    write_data()