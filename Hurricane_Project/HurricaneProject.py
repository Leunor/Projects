# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def f_update_damages(x):
  damages_updated = []
  for i in x:
    if i == "Damages not recorded":
      damages_updated.append("Damages not recorded")
    if i[-1] == "M":
      b = i.replace("M", "")
      a = float(b)*1000000
      damages_updated.append(a)
    if i[-1] == "B":
      b = i.replace("B", "")
      a = float(b)*1000000000
      damages_updated.append(a)
  return damages_updated
updated_damages = f_update_damages(damages)
print(updated_damages)

# write your construct hurricane dictionary function here:
def f_hurricane_dictionary(name, month, year, max_sustained_wind, area_affected, damage, death):
  hurricane_dict = {}
  for i in range(len(name)):
    hurricane_dict[name[i]] = {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Wind": max_sustained_wind[i], "Areas Affected": area_affected[i], "Damage": damage[i], "Deaths": death[i]}
  return hurricane_dict
hurricane_dictionary = f_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricane_dictionary)

# write your construct hurricane by year dictionary function here:
def f_new_hurricane_dict(x):
  new_hurricane_dictionary = {}
  for key,value in x.items():
    year = x[key]["Year"]
    if not new_hurricane_dictionary.get(year):
      new_hurricane_dictionary[year] = [value]
    else:
      new_hurricane_dictionary[year].append([value])
  return new_hurricane_dictionary
new_hurricane_dictionary = f_new_hurricane_dict(hurricane_dictionary)
print(new_hurricane_dictionary)
print(new_hurricane_dictionary[1932])

# write your count affected areas function here:
def f_count(x):
  count_areas = {}
  for areas in x:
    for area in areas:
      if count_areas.get(area):
        count_areas[area] += 1
        continue
      count_areas[area] = 1
  return count_areas
count_areas_affected = f_count(areas_affected)
print(count_areas_affected)
# write your find most affected area function here:
def f_max_count(x):
  count_areas_affected = f_count(x)
  count = 0
  most_affected = ""
  for key,value in count_areas_affected.items():
    if value > count:
      count = value
      most_affected = key
    else:
        continue
    return ("The most affected area is {} with {} hurricanes.").format(most_affected, count)

max_area_affected = f_max_count(areas_affected)
print(max_area_affected)

# write your greatest number of deaths function here:
def f_most_death_count(x):
  max_death = 0
  place = ""
  for key,value in x.items():
    death = value["Deaths"]
    if death > max_death:
      max_death = death
      place = key
    else:
      continue
  return ("The hurricane with the most deaths is {} with {} deaths.").format(place,max_death)

max_death = f_most_death_count(hurricane_dictionary)
print(max_death)

# write your catgeorize by mortality function here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def f_mortality(x):
  mortality_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for value in x.values():
    death = value["Deaths"]
    if death == 0:
      mortality_dictionary[0].append(value)
    elif 0 < death <= 100:
      mortality_dictionary[1].append(value)
    elif 100 < death <= 500:
      mortality_dictionary[2].append(value)
    elif 500 < death <= 1000:
      mortality_dictionary[3].append(value)
    elif 1000 < death <= 10000:
      mortality_dictionary[4].append(value)
    else:
      mortality_dictionary[5].append(value)
  return mortality_dictionary

mortality_rate = f_mortality(hurricane_dictionary)
print(mortality_rate)

# write your greatest damage function here:
def f_most_damage_count(x):
  max_damage = 0
  place = ""
  for key,value in x.items():
    damage = value["Damage"]
    if damage == "Damages not recorded":
      continue
    if damage > max_damage:
      max_damage = damage
      place = key
    else:
      continue
  return ("The hurricane with the most damage is {} with cost of {} dollars.").format(place,max_damage)

max_damage = f_most_damage_count(hurricane_dictionary)
print(max_damage)

# write your catgeorize by damage function here:
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
def f_rate_hurricane(x):
  rate_hurricane_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for value in x.values():
    damage = value["Damage"]
    if damage == "Damages not recorded":
      continue
    elif damage == 0:
      rate_hurricane_dictionary[0].append(value)
    elif 0 < damage <= 100000000:
      rate_hurricane_dictionary[1].append(value)
    elif 100000000 < damage <= 1000000000:
      rate_hurricane_dictionary[2].append(value)
    elif 1000000000 < damage <= 10000000:
      rate_hurricane_dictionary[3].append(value)
    elif 10000000000 < damage <= 50000000000:
      rate_hurricane_dictionary[4].append(value)
    else:
      rate_hurricane_dictionary[5].append(value)
  return rate_hurricane_dictionary

hurricane_rate = f_rate_hurricane(hurricane_dictionary)
print(hurricane_rate)
