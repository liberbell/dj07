from database import db_session
from models import Data
import pandas as pd

data = db_session.query(Data.date, Data.subscribers, Data.reviews)