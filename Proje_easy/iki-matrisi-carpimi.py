"""
İki matrisi çarpan bir program yazın 
(Write a program that multiplies two matrices).
"""

import numpy as np

def matris_carpimi(matris1, matris2):
    return np.dot(matris1,matris2)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
m = matris_carpimi(m1, m2)
print(m)