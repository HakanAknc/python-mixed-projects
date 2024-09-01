"""
Bu proje, belirli bir uzunluk ve karmaşıklıkta rastgele bir şifre oluşturan bir program oluşturmayı içerir.
"""

import random 
import string
import time

def generate_password():
    lower = input("Küçük harf mi kullanıyorsunuz? (E/H): ").lower()
    upper = input("Büyük harf mi kullanıyorsunuz? (E/H): ").upper()
    numbers = input("Numaraları mı kullanıyorsunuz? (E/H): ").lower()
    symbols = input("Özel karakterler mi kullanıyorsunuz? (E/H): ").lower()

    if lower == "h" and upper == "h" and numbers == "h" and symbols == "h":
        print("En az bir karakter türü seçmelisiniz!")
    else:
        selected_types = [lower, upper, numbers, symbols]
        selected_chars = [string.ascii_lowercase if lower == "e" else "",
                          string.ascii_uppercase if upper == "e" else "",
                          string.digits if numbers == "e" else "",
                          string.punctuation if symbols == "e" else ""]
        
        total_length = 0
        for chars in selected_chars:
            if chars:
                total_length += len(chars)

        print(f"Şifre uzunluğu en fazla {total_length} karakter uzunluğunda olmalıdır.")
        time.sleep(1)
        length = int(input("Şifrenin uzunluğunu girin: "))

        if length > total_length:
            print("Şifre uzunluğu çok uzun!")
            return
        
        all_chars = "".join(selected_chars)

        user_password = "".join(random.sample(all_chars, length))
        return user_password
    
user_password = generate_password()
print(user_password)