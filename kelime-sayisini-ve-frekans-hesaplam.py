"""
Verilen bir metindeki kelime sayısını ve frekanslarını hesaplayan bir program yazın (Write a program that calculates the word frequency and counts in a given text).
"""

import string

def word_count(text):
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.lower().split()

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return len(words), word_freq

text = "This is a sample text for testing word count. It should count each word and show its frequency."
print(word_count(text))