"""
Verilen bir listenin en büyük elemanını bulan bir program yazın 
(Write a program to find the largest element of a given list).
"""

def find_largest_element(lst):
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    return largest

numbers = [3, 4, 1, 0, 4, 8, 12]
largest_num = find_largest_element(numbers)
print(largest_num)