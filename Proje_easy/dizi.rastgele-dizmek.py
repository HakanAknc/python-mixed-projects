"""
Bir dizi elemanını rastgele sıraya dizmek için bir program yazın (Write a program to shuffle the elements of an array randomly).
"""

import random

def shuffle_array(arr):
    shuffled_arr = arr.copy()
    random.shuffle(shuffled_arr)
    return shuffled_arr

arr = [1, 2, 3, 4, 5]
print(shuffle_array(arr))