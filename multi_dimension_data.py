# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:27:30 2017

@author: yuguang
"""

#multi-dimension
import numpy as np
a = np.arange(100).reshape(10, 5, 2)
#a.tofile("b.dat", sep=",", format = '%d')
##c = np.loadtxt('b.dat', delimiter=',')
#d = np.fromfile("b.dat", dtype = np.int, sep = ",").reshape(10, 5, 2)#recovery data from file,need to know the data dimension and data type
#print(d) 

np.save("a.npy", a)
b = np.load("a.npy")
print(b)

#np.random.seed(10) shici sui ji shu xiang tong