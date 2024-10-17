"""
Bir dizinin elemanlarını tersten yazdıran bir program yazın
 (Write a program that prints the elements of an array in reverse order)
"""

def reverse_array(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_array(my_array)