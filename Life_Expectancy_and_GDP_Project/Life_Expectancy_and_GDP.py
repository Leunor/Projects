from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
%matplotlib inline

df = pd.read_csv("all_data.csv")
df.rename(columns={"Life expectancy at birth (years)" : "LEABY"}, inplace=True)
print(df.head())
print(df.Country.unique())
print(df.Year.unique())

#Distribution of Life Expectancy
plt.figure(figsize=(8,6))
sns.distplot(df["LEABY"], rug=True, kde=True) #curve shows KDE(Kernel Density Estimation)
plt.xlabel("Life expectancy at birth (years)")
plt.title("Distribution of Life Expectancy")
plt.show()

#Distribution of GDP
plt.figure(figsize=(8,6))
sns.distplot(df["GDP"], rug=True, kde=True) #curve shows KDE(Kernel Density Estimation)
plt.xlabel("GDP in Trillions of US Dollars")
plt.title("Distribution of GDP")
plt.show()

dfmean = df.drop("Year", axis = 1).groupby("Country").mean().reset_index()
print(dfmean)

#Has life expectancy increased over time in the six nations?
plt.figure(figsize=(8,6))
sns.barplot(data=dfmean, x="LEABY", y="Country")
plt.title("Life Expectancy in each Country")
plt.xlabel("Life expectancy at birth (years)")
plt.show()

#Has GDP increased over time in the six nations?
plt.figure(figsize=(8,6))
sns.barplot(data=dfmean, x="GDP", y="Country")
plt.xlabel("GDP in Trillions of U.S. Dollars")
plt.title("GDP in each Country")
plt.show()
