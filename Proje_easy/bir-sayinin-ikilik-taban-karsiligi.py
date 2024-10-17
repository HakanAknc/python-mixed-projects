"""
Bir sayının ikilik tabandaki karşılığını hesaplayan bir program yazın (Write a program that calculates the binary representation a number).
"""

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

print(decimal_to_binary(3410))