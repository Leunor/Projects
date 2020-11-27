# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)

plt.hist(flights, range = (0,365), bins = 365, edgecolor = 'black')
plt.title('Flight Count vs Time')
plt.xlabel('Day of the Year')
plt.ylabel('Flight Count')

plt.subplot(212)

plt.hist(in_bloom, range = (0,365), bins = 365, edgecolor = 'black')
plt.title('Bloom Count vs Flights by Day')
plt.xlabel('Day of the Year')
plt.ylabel('Bloom Count')
plt.tight_layout()

plt.show()
