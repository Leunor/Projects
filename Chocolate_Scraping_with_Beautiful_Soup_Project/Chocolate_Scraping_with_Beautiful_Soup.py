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

company_tags = soup.select(".Company")
company = []
for x in company_tags[1:]:
  company.append(x.get_text())
print(company)

percentage_tags = soup.select(".CocoaPercent")
cocoa_percentages = []
for x in percentage_tags[1:]:
  percentage = float(x.get_text().strip('%'))
  cocoa_percentages.append(percentage)
print(cocoa_percentages)


d = {"Company": company, "Rating": ratings, "CocoaPercentage": cocoa_percentages}
df = pd.DataFrame.from_dict(d)
avg = df.groupby("Company").Rating.mean()
ten_highest = avg.nlargest(10)
print(df)
print(avg)
print(ten_highest)

plt.clf()
plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
