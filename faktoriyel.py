"""
Girilen bir sayının faktöriyelini hesaplayan bir program yazın.
 (Write a program that calculates the factorial of a given number)
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
num = 5
print("Factorial of", num, "is", factorial(num))