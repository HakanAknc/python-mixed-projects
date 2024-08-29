"""
İki sayı arasındaki asal sayıları listeleyen bir program yazın 
(Write a program that lists the prime numbers between two given numbers).
"""

def prime_numbers(start, end):
    prime_nums = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums

start_num = 3
end_num = 99
prime_nums_res = prime_numbers(start_num, end_num)
print(f"Prime numbers between {start_num} and {end_num} are: {prime_nums_res}")