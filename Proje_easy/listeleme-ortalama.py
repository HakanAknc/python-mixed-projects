"""
Bir listedeki elemanların ortalamasını hesaplayan bir program yazın (Write a program that calculates the average of the elements in a lis
"""

def calculate_average(lst):
    return sum(lst) / len(lst)

numbers = [1,2,3,4,5]
print(calculate_average(numbers))