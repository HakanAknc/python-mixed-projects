"""
Bir cümledeki kelimelerin sayısını hesaplayan bir program yazın
(Write a program that counts the number of words in a sentence).
"""

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "Bugün git version kontrol konusunu öğrendim."
num_words = count_words(sentence)
print("Number of words: ", num_words)