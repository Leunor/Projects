# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
print(np.mean(chol_hd))
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

chol_no_hd = no_hd.chol
print(np.mean(chol_no_hd))
tstat, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)

num_patients = len(heart)
print(num_patients)

num_highfbs_patients = np.sum(heart.fbs == 1)
print(num_highfbs_patients)

print(0.08*num_patients)

pval = binom_test(num_highfbs_patients, n=num_patients, p=0.08, alternative='greater')
print(pval)


sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.show()
thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']
thalach_mean_difference =np.mean(thalach_no_hd) - np.mean(thalach_hd)
print('thalach mean Difference: ' + str(thalach_mean_difference))
thalach_median_difference = np.median(thalach_no_hd) - np.median(thalach_hd)
print('thalach median Difference: ' + str(thalach_median_difference))

from scipy.stats import ttest_ind
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
#“reject the null hypothesis” and conclude that there is a significant difference in thalach for people with heart disease compared to people without heart disease

#age
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()
age_hd = heart.age[heart.heart_disease == 'presence']
age_no_hd = heart.age[heart.heart_disease == 'absence']
mean_diff = np.mean(age_hd) - np.mean(age_no_hd)
print('age mean Difference: ', mean_diff)
med_diff = np.median(age_hd) - np.median(age_no_hd)
print('age median Difference: ', med_diff)
tstat, pval = ttest_ind(age_hd, age_no_hd)
print('p-value for age two-sample t-test: ', pval)

#trestbps
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.trestbps)
plt.show()
trestbps_hd = heart.trestbps[heart.heart_disease == 'presence']
trestbps_no_hd = heart.trestbps[heart.heart_disease == 'absence']
mean_diff = np.mean(trestbps_hd) - np.mean(trestbps_no_hd)
print('`trestbps` mean Difference: ', mean_diff)
med_diff = np.median(trestbps_hd) - np.median(trestbps_no_hd)
print('`trestbps` median Difference: ', med_diff)
tstat, pval = ttest_ind(trestbps_hd, trestbps_no_hd)
print('p-value for `trestbps` two-sample t-test: ', pval)

#chol
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.chol)
plt.show()
chol_hd = heart.chol[heart.heart_disease == 'presence']
chol_no_hd = heart.chol[heart.heart_disease == 'absence']
mean_diff = np.mean(chol_hd) - np.mean(chol_no_hd)
print('`chol` mean Difference: ', mean_diff)
med_diff = np.median(chol_hd) - np.median(chol_no_hd)
print('`chol` median Difference: ', med_diff)
tstat, pval = ttest_ind(chol_hd, chol_no_hd)
print('p-value for `chol` two-sample t-test: ', pval)

plt.clf()
sns.boxplot(x=heart.cp, y=heart.thalach)
plt.show()
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']
from scipy.stats import f_oneway
fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print('p-value for ANOVA: ', pval)

from statsmodels.stats.multicomp import pairwise_tukeyhsd
result = pairwise_tukeyhsd(heart.thalach, heart.cp, 0.05)
print(result)

from scipy.stats import chi2_contingency
table = pd.crosstab(heart.cp, heart.heart_disease)
print(table)
chi2, pval, dof, expected = chi2_contingency(table)
print('p-value for chi-square test: ', pval)
