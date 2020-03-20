# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 07:48:38 2019

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
# In[] Put Variables Here
# Theta in degress
theta = 23
# Gravity in m/s/s
g = 9.81
#change in position in m
x = 1.205
#margin of error
e = .95

# In[]



raw_data = np.load(r"C:\Users\ASUS\Desktop\PhysicsLAb\Data\26deg.npy").reshape(-1).tolist()
data_list = []
for i in raw_data:
    if i >.05:
        data_list.append(i)
data_list = np.array(data_list).reshape(-1)

num_bins = 15
n, bins, patches = plt.hist(data_list, num_bins, density=1, facecolor='Green', alpha=0.5)




y = mlab.normpdf(bins, np.mean(data_list), np.std(data_list))
plt.plot(bins, y, 'r--')
plt.xlabel('Time in seconds')
plt.ylabel('Probability')
plt.title(r'Histogram of Times')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()

confidence = (norm.ppf(e))*(np.std(data_list)/np.sqrt(len(data_list)))



# In[]

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("The average time was:"+str(np.mean(data_list)))

final_awnser = (math.tan(math.radians(theta)))-((2*x)/(np.mean(data_list)*np.mean(data_list)*(g*math.cos(math.radians(theta)))))
print("The coefficent of friction for these results is:" + str(final_awnser))
print("The standard deviation of the times was:" + str(np.std(data_list)))
print("Margin of error with "+ str(e)[2:]+"% confidence:" + str(confidence))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")