import codecademylib3_seaborn
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
def n_ranking(n, data):
  find_rank = data[data["Rank"] <= n]
  for coaster in set(find_rank["Name"]):
    coaster_rankings = find_rank[find_rank['Name'] == coaster]
    ax = plt.subplot()
    x_axis = coaster_rankings["Year of Rank"]
    y_axis = coaster_rankings["Rank"]
    plt.plot(x_axis, y_axis, marker = "o",label=coaster)
  plt.xlabel("Year")
  plt.ylabel("Rank")
  plt.title("Top " + str(n) + " Coasters")
  ax.invert_yaxis()
  ax.set_yticks(range(1, n+1))
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
  return plt.show()

n_ranking(4, wood)

plt.clf()

# load roller coaster data here:
captain_coaster = pd.read_csv("roller_coasters.csv")
print(captain_coaster)

# write function to plot histogram of column values here:
def plot_hist(name, data):
  if name == "height":
    heights = data[data["height"] <= 140]
    value = heights[name].dropna()
  else:
    value = data[name].dropna()
  plt.hist(value, bins = 15)
  plt.legend()
  plt.title(name.title() + " Histogram")
  plt.xlabel(name.title())
  plt.ylabel("Count")
  return plt.show()

plot_hist("length", captain_coaster)

plt.clf()

# write function to plot inversions by coaster at a park here:
def num_inversions(park, data):
  park_coasters = data[data['park'].str.contains(park,case=False)].sort_values('num_inversions', ascending=False)
  coaster_names = park_coasters['name']
  number_inversions = park_coasters['num_inversions']
  ax = plt.subplot()
  plt.bar(range(len(number_inversions)),number_inversions)
  plt.xlabel("Roller Coaster")
  plt.ylabel("Number of Inversions")
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names, rotation=90)
  return plt.show()

num_inversions('Holiday Park', captain_coaster)

plt.clf()

# write function to plot pie chart of operating status here:
def operate_status(data):
  num_operating = data[data.status == 'status.operating']
  num_closed = data[data.status == 'status.closed.definitely']
  count_operating = [len(num_operating), len(num_closed)]
  plt.pie(count_operating, autopct='%0.1f%%', labels=['Operating','Closed'])
  #plt.figure(figsize=[10,10])
  plt.title("Operating vs Closed")
  plt.legend()
  plt.axis('equal')
  return plt.show()

operate_status(captain_coaster)

plt.clf()

# write function to create scatter plot of any two numeric columns here:
def scatter_plot(data, column1, column2):
  if column1 != 'height' and column2 != 'height':
    col1 = data[column1]
    col2 = data[column2]
  else:
    data = data[data['height'] < 140]
    col1 = data[column1]
    col2 = data[column2]
  ax = plt.subplot()
  plt.figure(figsize=[10,8])
  plt.scatter(col1, col2)
  plt.xlabel(column1.title())
  plt.ylabel(column2.title())
  plt.title(column1 + " vs " + column2)
  return plt.show()

scatter_plot(captain_coaster, 'speed', 'height')

plt.clf()

#Most Popular Seats
def seating(data):
  clean_data = data.dropna()
  seat_type = clean_data['seating_type'].unique()
  pie_plot = []
  for i in seat_type:
    value = clean_data[clean_data['seating_type'] == i]
    pie_plot.append(len(value))
  plt.figure(figsize=[10,10])
  plt.pie(pie_plot, autopct='%0.1f%%')
  plt.axis('equal')
  plt.title('Distribution of Seat Types')
  plt.legend(seat_type)
  plt.show()

seating(captain_coaster)

plt.clf()
