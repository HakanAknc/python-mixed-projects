import random

def sayi_tahmin_oyunu():
    rastgele_Sayi = random.randint(1, 100)
    tahmin_hakki = 7

    print("1 ile 100 arasında bir sayı seçtim. Hadi tahmin et bakalım!")

    while tahmin_hakki > 0:
        print(f"\nKalan tahmin hakkın: {tahmin_hakki}")
        tahmin = input("Bir sayı tahmin edin: ")

        try:
            tahmin = int(tahmin)
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        tahmin_hakki -= 1

        if tahmin < rastgele_Sayi:
            print("Daha büyük bir sayı gir!")
        elif tahmin > rastgele_Sayi:
            print("Daha küçük bir sayı gir!")
        else:
            print(f"Tebrikler! Sayıyı doğru tahmin ettin: {rastgele_Sayi}")
            break

    if tahmin_hakki == 0:
        print(f"Maalesef tahmin hakkın bitti. Doğru sayı: {rastgele_Sayi}")

sayi_tahmin_oyunu()
