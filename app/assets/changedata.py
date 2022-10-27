import models
import pandas as pd

from database import db_session

df = pd.read_csv("data.csv")
print(df.head())