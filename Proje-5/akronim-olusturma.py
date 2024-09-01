"""
Bu proje, bir cümleyi veya kelime öbeğini alıp her kelimenin ilk harfinden bir akronim oluşturan bir program oluşturmayı içerir.
"""

def create_acronym(user_text):
    words = user_text.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

user_text = input("Lütfen bir cümle veya ifade girin: ")
print(create_acronym(user_text))