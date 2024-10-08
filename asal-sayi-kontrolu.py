"""
Verilen bir sayının asal olup olmadığını kontrol eden bir program yazın
(Write a program that checks whether a given number is prime or not).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(10))
print(is_prime(17))