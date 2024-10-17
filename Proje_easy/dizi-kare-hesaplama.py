"""
Bir dizideki her elemanın karesini hesaplayan bir program yazın (Write a program that calculates the square of each element in an array).
"""

def square_elements(lst):
    return [x**2 for x in lst]

numbers = [1,2,3,4,5]
print(square_elements(numbers))