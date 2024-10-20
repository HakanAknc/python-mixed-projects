import random
import string

def sifre_olusturma(uzunluk):
    karekterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karekterler) for _ in range(uzunluk))
    return sifre


while True:
    try:
        uzunluk = int(input("Şifrenizin uzunluğu kaç karekter olsun? (Min8): "))
        if uzunluk < 8:
            print("Lütfen en az 8 karekterli bir sifere belirleyin.")
            continue
        else:
            olusturulan_sifre = sifre_olusturma(uzunluk)
            print(f"Olusturulan sifre: {olusturulan_sifre}")
            break
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        