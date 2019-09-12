# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt

W1 = np.array([[0,0,1,1],
               [0,1,0,1]])
W2 = np.array([[2,2,3,3],
               [0,1,0,1]])

def barycentre(data):
    return [np.mean(data[0,:]), np.mean(data[1,:])]            
    
def getNormal(M1, M2):
    dir = np.transpose(M2) +  (-1)*np.transpose(M1)
    rslt = [-1*dir[1], dir[0]]  
    return rslt

def getM(M1, M2):
    return [(M1[0] + M2[0])/2, (M1[1] + M2[1])/2]
    
    
"""
Produit matriciel
np.dot(,)
"""
M1 = (barycentre(W1))
M2 = (barycentre(W2))

M = getM(M1, M2)
C1 = (np.dot(A, (W1-M)) >= 0)
C2 = (np.dot(A, (W2-M)) >= 0)


print(barycentre(W1))
print(barycentre(W2))
print(getNormal(barycentre(W1),barycentre(W2)))
print(getM(barycentre(W1),barycentre(W2)))


plt.plot(W1[0], W1[1], 'ro', label = "W1")
plt.plot(W2[0], W2[1], 'bo', label = "W2")
plt.plot(barycentre(W1)[0], barycentre(W1)[1], 'rs', label = "barycentre de W1")
plt.plot(barycentre(W2)[0], barycentre(W2)[1], 'bs', label = "barycentre de W2")
plt.plot(getM(barycentre(W1),barycentre(W2))[0], 
         getM(barycentre(W1),barycentre(W2))[1], 'gs')
plt.plot([1.5,1.5],[-0.5,1.5], 'g--')
plt.axis((-0.5, 3.5, -0.5, 1.5))
plt.legend()         
plt.show()