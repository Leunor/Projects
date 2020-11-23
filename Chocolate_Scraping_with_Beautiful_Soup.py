import seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content, "html.parser")
#print(soup)
rating_tags = soup.find_all(attrs={"class": "Rating"})
ratings = []

for rating in rating_tags[1:]:
  ratings.append(float(rating.get_text()))

print(ratings)
plt.hist(ratings)
plt.show()
