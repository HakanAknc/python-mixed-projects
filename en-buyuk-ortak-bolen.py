"""
İki sayının en büyük ortak bölenini bulan bir program yazın 
(Write a program to find the greatest common divisor of two numbers).
"""

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
    
print(gcd(30, 36))