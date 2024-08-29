"""
Verilen bir listedeki elemanları tekrar etmeden sıralayan bir program yazın
(Write a program that sorts the elements of a list without duplicates).
"""

def sort_list_without_repeats(lst):
    return list(sorted(set(lst)))

numbers = [1,4,6,8,4,3,2,2,5,7,8,9,1,2,0,2,4]
print(sort_list_without_repeats(numbers))