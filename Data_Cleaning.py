import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn
import glob

us_census_files = glob.glob("states*.csv")
data_list = []

for files in us_census_files:
  read = pd.read_csv(files)
  data_list.append(read)

us_census = pd.concat(data_list)
#print(data)

#turn income from strings to floats 1
us_census.Income= us_census.Income.replace('[\$,]', '', regex = True)
us_census.Income = pd.to_numeric(us_census.Income)
#turn income from strings to floats method 2
#data_income = us_census.Income.replace('\$+', expand = True)
#print(data_income)
#us_census.Income = pd.to_numeric(data_income[1])

data_gender_pop = us_census.GenderPop.str.split('(\d+)', expand = True)


us_census['Men'] = data_gender_pop[1]
us_census['Women'] = data_gender_pop[3]
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)

#print(data_gender_pop)

pyplot.scatter(us_census.Women, us_census.Income)
pyplot.show()

print(us_census.Women.count())
us_census = us_census.fillna(value = {'Women': us_census.TotalPop - us_census.Men})

us_census = us_census[['State', 'TotalPop', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'Income',	'Men', 'Women']]

#print(data)
duplicates = us_census.duplicated()
print(duplicates.value_counts())

us_census = us_census.drop_duplicates()
print(us_census.duplicated().value_counts())
print(us_census)

pyplot.close()
pyplot.scatter(us_census.Women, us_census.Income)
pyplot.xlabel('Women')
pyplot.ylabel('Income')
pyplot.show()

us_census.Hispanic = pd.to_numeric(us_census.Hispanic.replace('[\%]', '', regex=True))
us_census.White = pd.to_numeric(us_census.White.replace('[\%]', '', regex=True))
us_census.Black = pd.to_numeric(us_census.Black.replace('[\%]', '', regex=True))
us_census.Native = pd.to_numeric(us_census.Native.replace('[\%]', '', regex=True))
us_census.Asian = pd.to_numeric(us_census.Asian.replace('[\%]', '', regex=True))
us_census.Pacific = pd.to_numeric(us_census.Pacific.replace('[\%]', '', regex=True))

us_census = us_census.fillna(value={
'Hispanic': us_census.Hispanic.mean(),
'White': us_census.White.mean(),
'Black': us_census.Black.mean(),
'Native': us_census.Native.mean(),
'Asian': us_census.Asian.mean(),
'Pacific': us_census.Pacific.mean(),
})
print(us_census)

pyplot.hist(us_census.Hispanic)
pyplot.title('Hispanic')
pyplot.show()

pyplot.hist(us_census.White)
pyplot.title('White')
pyplot.show()

pyplot.hist(us_census.Black)
pyplot.title('Black')
pyplot.show()

pyplot.hist(us_census.Native)
pyplot.title('Native')
pyplot.show()

pyplot.hist(us_census.Asian)
pyplot.title('Asian')
pyplot.show()

pyplot.hist(us_census.Pacific)
pyplot.title('Pacific')
pyplot.show()
