import csv
with open("insurance.csv") as insurance_csv:
    print(insurance_csv.read())
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
def data(lst, csv_file, column):
    with open(csv_file) as insurance_csv:
        csv_dict = csv.DictReader(insurance_csv)
        for person in csv_dict:
            lst.append(person[column])
        return lst

data(age, "insurance.csv", 'age')
data(sex, "insurance.csv", 'sex')
data(bmi, "insurance.csv", 'bmi')
data(children, "insurance.csv", 'children')
data(smoker, "insurance.csv", 'smoker')
data(region, "insurance.csv", 'region')
data(charges, "insurance.csv", 'charges')

class PatientsInfo:
    def __init__(self, p_age, p_sex, p_bmi, p_children, p_smoke, p_region, p_charges):
        self.p_age = p_age
        self.p_sex = p_sex
        self.p_bmi = p_bmi
        self.p_children = p_children
        self.p_smoke = p_smoke
        self.p_region = p_region
        self.p_charges = p_charges

    def average_age(self):
        total = 0
        for i in self.p_age:
            a = float(i)
            total += a
        print("Average Age: " + str("%.2f"%(total/len(age))))

    def count_sexes(self):
        count_male = 0
        count_female = 0
        for i in self.p_sex:
            if i == 'male':
                count_male += 1
            elif i == 'female':
                count_female += 1
        print("Number of Males: " + str(count_male))
        print("Number of Females: " + str(count_female))

    def count_regions(self):
        location = []
        unique_regions = []
        nw = 0
        ne = 0
        sw = 0
        se = 0
        for i in self.p_region:
            if i == 'northwest':
                nw += 1
            elif i == 'northeast':
                ne += 1
            elif i == 'southwest':
                sw += 1
            elif i == 'southeast':
                se += 1
        print("North West: " + str(nw))
        print("North East: " + str(ne))
        print("South West: " + str(sw))
        print("South East: " + str(se))

    def unique_regions(self):
        unique_regions = []
        for region in self.p_region:
            if region not in unique_regions:
                unique_regions.append(region)
        print("Number of unique regions: " + str(unique_regions))

    def average_charges(self):
        total = 0
        for i in self.p_charges:
            a = float(i)
            total += a
        print("Average Yearly Medical Charges: $" + str("%.2f"%(total/len(age))))

    def create_dict(self):
        self.p_dict = {}
        self.p_dict["Age"] = [int(age) for age in self.p_age]
        self.p_dict["Sex"] = self.p_sex
        self.p_dict["BMI"] = self.p_bmi
        self.p_dict["Children"] = self.p_children
        self.p_dict["Smoker"] = self.p_smoke
        self.p_dict["Region"] = self.p_region
        self.p_dict["Charges"] = self.p_charges
        print(self.p_dict)

patient_info = PatientsInfo(age, sex, bmi, children, smoker, region, charges)
patient_info.average_age()
patient_info.count_sexes()
patient_info.count_regions()
patient_info.unique_regions()
patient_info.average_charges()
patient_info.create_dict()
