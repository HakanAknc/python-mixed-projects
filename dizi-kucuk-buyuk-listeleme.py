"""
Bir dizinin elemanlarını küçükten büyüğe sıralayan bir program yazın
(Write a program that sorts the elements of an array in ascending order).
"""

def sort_array(arr):
    return sorted(arr)

my_list = [3,6,1,8,2,0,5]
sorted_list = sort_array(my_list)
print(sorted_list)