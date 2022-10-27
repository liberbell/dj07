import models
import pandas as pd
import datetime

from database import db_session

df = pd.read_csv("data.csv")
print(df.head())

print(type(df.iloc[0, 0]))
fdate = datetime.datetime.strptime(df.iloc[0, 0], "%Y/%m/%d").date()
print(fdate, type(fdate))