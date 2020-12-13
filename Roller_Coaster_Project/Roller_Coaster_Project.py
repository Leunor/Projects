import seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")

print(wood.head(20))
print(steel.head(20))

# write function to plot rankings over time for 1 roller coaster here:
def roller_coaster_ranking(name, park, data):
  find_rank = data[(data["Name"] == name) & (data["Park"] == park)]
  x_axis = find_rank["Year of Rank"]
  y_axis = find_rank["Rank"]
  ax = plt.subplot()
  plt.plot(x_axis, y_axis, marker = "o")
  plt.xlabel("Year")
  plt.ylabel("Rank")
  plt.title("Rank of " + str(name) + " vs Year")
  ax.set_xticks(x_axis.values)
  ax.set_yticks(y_axis.values)
  ax.invert_yaxis()
  return plt.show()
roller_coaster_ranking("El Toro", "Six Flags Great Adventure", wood)

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_roller_coaster_ranking(name1, park1, name2, park2, data):
  find_rank1 = data[(data["Name"] == name1) & (data["Park"] == park1)]
  find_rank2 = data[(data["Name"] == name2) & (data["Park"] == park2)]
  x_axis1 = find_rank1["Year of Rank"]
  y_axis1 = find_rank1["Rank"]
  x_axis2 = find_rank2["Year of Rank"]
  y_axis2 = find_rank2["Rank"]
  ax = plt.subplot()
  plt.plot(x_axis1, y_axis1, marker = "o", label = name1)
  plt.plot(x_axis2, y_axis2, marker = "x", label = name2)
  plt.xlabel("Year")
  plt.ylabel("Rank")
  plt.title( str(name1) + " vs " + str(name2) + " Rankings")
  ax.set_xticks(x_axis1.values)
  ax.set_yticks(pd.concat([y_axis1, y_axis2]).drop_duplicates().values)
  ax.set_yticklabels(pd.concat([y_axis1, y_axis2]).drop_duplicates().values)
  ax.invert_yaxis()
  plt.legend()
  return plt.show()
two_roller_coaster_ranking("El Toro", "Six Flags Great Adventure", "Boulder Dash", "Lake Compounce", wood)

plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
