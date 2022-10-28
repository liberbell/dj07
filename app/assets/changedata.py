import models
import pandas as pd
import datetime

from database import db_session

df = pd.read_csv("data.csv")
# print(df.head())

# print(type(df.iloc[0, 0]))
fdate = datetime.datetime.strptime(df.iloc[0, 0], "%Y/%m/%d").date()
# print(fdate, type(fdate))

for index, _df in df.iterrows():
    fdate = datetime.datetime.strptime(_df["date"], "%Y/%m/%d").date()
    print(_df["date"])
    row = models.Data(date=date, subscribers=_df["subscribers"], reviews=_df["reviews"])
    db_session.add(row)
    
db_session.commit()