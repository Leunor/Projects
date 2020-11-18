def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking")
  else:
    print("Smoking is not an issue for you")

def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")

def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)
# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = "Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)
# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]

insurance_data = list(zip(names, insurance_costs))
print("Here is the actual insurance cost data: " + str(insurance_data))

estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

names.append("Priscilla")
insurance_costs.append(8320.0)
medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

total_cost = 0
for insurance in actual_insurance_costs:
  total_cost += insurance

average_cost = total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is below average.")
  else:
    print("The insurance cost for " + name + " is equal to the average.")

updated_estimated_costs = [x*11/10 for x in estimated_insurance_costs]

print(updated_estimated_costs)


medical_data = \
"""Marina Allison   ,27   ,   31.1 ,
#7010.0   ;Markus Valdez   ,   30,
22.4,   #4050.0 ;Connie Ballard ,43
,   25.3 , #12060.0 ;Darnell Weber
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1
,#3022.0   ;   Vinay Padilla,24,
26.9 ,#4620.0 ;Meredith Santiago, 51   ,
29.3 ,#16330.0;   Andre Mccarty,
19,22.7 , #2900.0 ;
Lorena Hodson ,65, 33.1 , #19370.0;
Isaac Vu ,34, 24.8,   #7045.0"""

#print(medical_data)
updated_medical_data = medical_data.replace('#', '$')
#print(updated_medical_data)
num_records = 0
for i in updated_medical_data:
  if i == "$":
    num_records += 1
print("There are " + str(num_records) + " medical records in the data.")

medical_data_split = updated_medical_data.split(";")
#print(medical_data_split)
medical_records1 = []
for record in medical_data_split:
    medical_records1.append(record.split(","))
#print(medical_records)
medical_records_clean = []
for record in medical_records1:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
print(medical_records_clean)
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

names = []
ages = []
bmis = []
insurance_costs = []
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = total_bmi/len(bmis)
print("Average BMI: " + str("%.2f"%(average_bmi)))
#or print("Average BMI: " + str(round(average_bmi,2))))

medical_costs = {}
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
medical_costs["Vinay"] = 3325.0
print(medical_costs)

total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

average_cost = total_cost/len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)
names_to_ages = {name:age for name,age in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get("Marina", None)
print("Marina's age is " + str(marina_age))

medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)

print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")
medical_records.pop("Vinay")

for key,value in medical_records.items():
  print(("{} is a {} year old {} {} with a BMI of {} and insurance cost of {}").format(key, value["Age"], value["Sex"], value["Smoker"], value["BMI"], value["Insurance_cost"]))


class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  def estimated_insurance_cost(self):
    estimated_cost = 250*self.age - 128*self.sex + 370*self.bmi + 425*self.num_of_children + 24000*self.smoker - 12500
    print(("{}'s estimated insurance cost is {} dollars.").format(self.name,str(estimated_cost)))
  def update_age(self, new_age):
    self.age = new_age
    print(("{} is now {} years old.").format(self.name, self.age))
    self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(("{} has {} child.").format(self.name, self.num_of_children))
    else:
      print(("{} has {} children.").format(self.name, self.num_of_children))
    self.estimated_insurance_cost()

  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information



patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)

print(patient1.patient_profile())
