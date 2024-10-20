import math

while True:

    girdi = input("İlk sayıyı girin (veya 'çıkış' yazın): ")

    if girdi.lower() == "çıkış":
        print("Programdan çıkılıyıor...")
        break

    try:
        sayi1 = float(girdi)
    except ValueError:
        # Eğer kullanıcı 'çıkış' yazarsa döngüden çık
        print("Programlamadan çıkılıyor...")
        continue

    sayi2 = None

    islem = input("Yapmak istediğiniz işlem nedir? (+, -, *, /, **, √, %): ")

    if islem == "√":
        sonuc = math.sqrt(sayi1)
    else:
        try:
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
            continue

        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
            else:
                sonuc = "Hata: 0'a bölme yapılamaz!"
        elif islem == "**":
            sonuc = sayi1 ** sayi2  # üslü işlem
        elif islem == "%":
            sonuc = sayi1 % sayi2
        else:
            sonuc = "Geçersiz işlem!"

    print(f"Sonuc: {sonuc}")

