# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:48:55 2019

@author: ASUS
"""
import numpy as np
dat_list = [1.01192,1.076446,1.106296,1.110754,1.122487,1.023837,1.042836,1.023881,0.984253,1.002414,0.966313,0.940516]
dat_list = np.array(dat_list)
np.save("31deg",dat_list)
np.savetxt("31deg.txt",dat_list)