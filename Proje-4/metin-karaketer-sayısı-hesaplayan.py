"""
Bu proje, belirli bir metindeki kelime ve karakter sayısını sayan bir program oluşturmayı içerir.
"""

user_text = input("Lütfen bir mein girin: ")
count_type = input("Kelimeleri (W) mi yoksa karakterleri (C) mi saymak istiyorsunuz? (WC): ")

if count_type.lower() == "w":
    word_count = len(user_text.split())
    print("Metindeki kelime sayısı: {}".format(word_count))
elif count_type.lower == "c":
    char_count = len(count_type)
    print("Metindeki karakter sayısı: {}".format(char_count))
else:
    print("Lütfen sayma türü olarak 'W' veya 'C'yi seçin.")