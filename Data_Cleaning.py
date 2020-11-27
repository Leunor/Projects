import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn
import glob

us_census = glob.glob("states*.csv")
data_list = []

for i in us_census:
  read = pd.read_csv(i)
  data_list.append(read)

data = pd.concat(data_list)
#print(data)

#turn income from strings to floats 1
data.Income= data.Income.replace('[\$,]', '', regex = True)
data.Income = pd.to_numeric(data.Income)
#turn income from strings to floats method 2
#data_income = data.Income.replace('\$+', expand = True)
#print(data_income)
#data.Income = pd.to_numeric(data_income[1])

data_gender_pop = data.GenderPop.str.split('(\d+)', expand = True)


data['Men'] = data_gender_pop[1]
data['Women'] = data_gender_pop[3]
data.Men = pd.to_numeric(data.Men)
data.Women = pd.to_numeric(data.Women)

#print(data_gender_pop)

pyplot.scatter(data.Women, data.Income)
pyplot.show()

print(data.Women.count())
data = data.fillna(value = {'Women': data.TotalPop - data.Men})

data = data[['State', 'TotalPop', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'Income',	'Men', 'Women']]

print(data)
duplicates = data.duplicated()
print(duplicates.value_counts())

data = data.drop_duplicates()
print(data.duplicated().value_counts())
print(data)

print(data.dtypes)
