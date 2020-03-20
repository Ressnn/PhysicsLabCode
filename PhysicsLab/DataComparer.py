# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:29:24 2019

@author: ASUS
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import math

from scipy import stats
# In[]
data_list = [np.load(r"C:\Users\ASUS\Desktop\PhysicsLAb\Data\25deg.npy").reshape(-1).tolist(),np.load(r"C:\Users\ASUS\Desktop\PhysicsLAb\Data\31deg.npy").reshape(-1).tolist(),np.load(r"C:\Users\ASUS\Desktop\PhysicsLAb\Data\39deg.npy").reshape(-1).tolist(),np.load(r"C:\Users\ASUS\Desktop\PhysicsLAb\Data\48deg.npy").reshape(-1).tolist()]
degrees = [25,31,39,48]
means = []
fv = []

g = 9.81
#change in position in m
x = 1.205
#margin of error
e = .95

np_data = []
for i in data_list:
    np_data.append(i[-12:])
    print(len(np_data[-1]))
np_data = np.array(np_data)

friction_coefficient = []
adj_list = []
for i in range(len(np_data)):
    for a in np_data[i]:
        theta = degrees[i]
        friction_coefficient.append((math.tan(math.radians(theta)))-((2*x)/(a*a*(g*math.cos(math.radians(theta))))))
        print(friction_coefficient[-1])
        adj_list.append((friction_coefficient[-1],theta,.100*math.cos(math.radians(theta))*g,.100*math.cos(math.radians(theta))*g*friction_coefficient[-1]))
adj_list = np.array(adj_list)
# In[]
num_bins = 15
n, bins, patches = plt.hist(friction_coefficient, num_bins, density=1, facecolor='Green', alpha=0.5)




y = mlab.normpdf(bins, np.mean(friction_coefficient), np.std(friction_coefficient))
plt.plot(bins, y, 'r--')
plt.xlabel('Coefficent of Friction')
plt.ylabel('Probability')
plt.title('Distribution of the calculated coefficents of friction')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
# In[]

line =  0.31137303031257085*adj_list[:,2]

plt.plot(adj_list[:,2],adj_list[:,3],'o', adj_list[:,2], line)

adj_list=np.array(adj_list)
plt.scatter(adj_list[:,2],adj_list[:,3])

plt.xlabel('Normal Force')
plt.ylabel('Force of Friction')
plt.title('Relationship between Normal Force and Friction')
plt.legend(("Scatterplot Points","best-fit line(no intercept) y= 0.3114x"))