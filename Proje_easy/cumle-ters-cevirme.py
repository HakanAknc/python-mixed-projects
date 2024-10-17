"""
Bir cümleyi tersine çeviren bir program yazın (Write a program that reverses a sentence).
"""

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence("If your code works fine don't touch it"))