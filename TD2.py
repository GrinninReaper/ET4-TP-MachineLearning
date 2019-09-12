# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:54:13 2019

@author: acandas
"""

import numpy as np
import matplotlib.pyplot as plt

#x@a produit matriciel de x par a
#np.hstack ou vstack pour metttre bout à bout les données

w1 = np.array([[1, 1], [0, 0], [0, 1]]);
w2 = np.array([[-1, -1, -1, -1], [-1, -1, -4, -4], [-0, -1, -0, -1]])

W1 =  np.array([[1, 1], [0, 0], [0, 1]])
W2 =  np.array([[-1, -1, -1], [0, 1, 1, 4 , 4], [0.5, 0, 1, 0, 1]])

def algo1(data1, data2):
    a0 = np.array([1, 0, 0])
    data = np.hstack((w1, w2))
    for i in range(10):
        for j in range(5):
            if(np.dot(a0, data[:, j]) <= 0):
                a0 = a0 + data[:, j]
                break
        if(j == len(data[0])):
            print("Found it")
            return a0
    return a0
    
def algo2(data1, data2):
    a0 = np.array([1, 0, 0])
    data = np.hstack((data1, data2))
    modified = 0
    for i in range(10):
        modified = 0
        for j in range(5):
            if(np.dot(a0, data[:, j]) <= 0):
                a0 = a0 + data[:, j]
                modified = 1
        if(modified == 0):
            print("Found it")
            return a0
    return a0

#
#print(w1);
#print(w2);
#print(np.hstack((w1,w2)))   
#print(algo1(w1, w2));
print(algo2(w1, w2));