"""
Verilen bir listedeki çift sayıların toplamını hesaplayan bir program yazın
(Write a program that calculates the sum of even numbers in a given list).
"""

def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(my_list)
print(result)