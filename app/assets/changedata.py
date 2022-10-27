import models
import pandas as pd

from database import db_session

df = pd.read_csv("assets/data.csv")
print(df.head())