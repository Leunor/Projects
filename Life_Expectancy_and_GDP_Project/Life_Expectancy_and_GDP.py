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
#Has GDP increased over time in the six nations?
#Is there a correlation between GDP and life expectancy of a country?
#What is the average life expectancy in these nations?
#What is the distribution of that life expectancy?

plt.figure(figsize=(8,6))
sns.barplot(data=dfmean, x="LEABY", y="Country")
plt.title("Life Expectancy in each Country")
plt.xlabel("Life expectancy at birth (years)")
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(data=dfmean, x="GDP", y="Country")
plt.xlabel("GDP in Trillions of U.S. Dollars")
plt.title("GDP in each Country")
plt.show()

f, ax = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
ax[0] = sns.violinplot(ax=ax[0], data=df, x="GDP", y="Country")
ax[0].set_xlabel("GDP in Trillions of US Dollars")
ax[1] = sns.violinplot(ax=ax[1], data=df, x="LEABY", y="Country")
ax[1].set_xlabel("Life expectancy at birth (years)")

f, ax = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
ax[0] = sns.swarmplot(ax=ax[0], data=df, x="GDP", y="Country")
ax[0].set_xlabel("GDP in Trillions of U.S. Dollars")
ax[1] = sns.swarmplot(ax=ax[1], data=df, x="LEABY", y="Country")
ax[1].set_xlabel("Life expectancy at birth (years)")

f, ax = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
ax[0] = sns.violinplot(ax=ax[0], data=df, x="GDP", y="Country", color = "black")
ax[0] = sns.swarmplot(ax=ax[0], data=df, x="GDP", y="Country")
ax[0].set_xlabel("GDP in Trillions of U.S. Dollars")
ax[1] = sns.violinplot(ax=ax[1], data=df, x="LEABY", y="Country", color = "black")
ax[1] = sns.swarmplot(ax=ax[1], data=df, x="LEABY", y="Country")
ax[1].set_xlabel("Life expectancy at birth (years)")

fig = plt.figure(figsize = (15,5))
ax1 = plt.subplot(1,2,1)
sns.lineplot(data=df, x="Year", y="GDP", hue="Country", legend=False)
plt.ylabel("GDP in Trillions of US Dollars")

ax2 = plt.subplot(1,2,2)
sns.lineplot(data=df, x="Year", y="LEABY", hue="Country")
plt.legend(labels=[i for i in df.Country.unique()],loc='lower left', bbox_to_anchor=(-0.6, 1, 1, 0.5), ncol=3)
plt.ylabel("Life expectancy at birth (years)")

plt.show()

graphGDP = sns.FacetGrid(df, col="Country", col_wrap=3, hue = "Country", sharey = False)
graphGDP = (graphGDP.map(sns.lineplot,"Year","GDP")
         .add_legend().set_axis_labels("Year","GDP in Trillions of U.S. Dollars"))

plt.show()

graphLEABY = sns.FacetGrid(df, col="Country", col_wrap=3, hue = "Country", sharey = False)
graphLEABY = (graphLEABY.map(sns.lineplot,"Year","LEABY")
         .add_legend().set_axis_labels("Year","Life expectancy at birth (years)"))

plt.show()

sns.scatterplot(data=df, x="LEABY", y="GDP", hue="Country")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.show()

graph = sns.FacetGrid(df, col="Country", col_wrap=3, hue = "Country", sharey = False, sharex = False)
graph = (graph.map(sns.scatterplot,"LEABY", "GDP")
         .add_legend().set_axis_labels("Life expectancy at birth (years)", "GDP in Trillions of U.S. Dollars"));
plt.show()
