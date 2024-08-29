"""
Verilen bir cümledeki en sık tekrar eden kelimeyi bulan bir program yazın (Write a program that finds the most frequently occurring word in a given sentence).
"""

from collections import Counter

def most_common_word(sentence):
    words = sentence.split()
    word_count = Counter(words)
    return word_count.most_common(1)[0][0]

sentence = "Next time there won't be a next time." #Phil Leotardo, in The Sopranos
print(most_common_word(sentence))