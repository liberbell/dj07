from operator import imod
from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-begginer.herokuapp.com/udemy"

data1 = requests.get(URL)