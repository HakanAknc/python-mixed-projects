"""
Verilen bir sayıyı verilen üsle hesaplayan bir program yazın (Write a program that calculates a given number raised to a given power).
"""

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(2,7))