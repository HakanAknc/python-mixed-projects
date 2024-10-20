def kelime_sayaci(metin):
    # Metni küçük harflere çevir ve noktalama işaretlerinden temizle
    metin = metin.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')

    # Kelimeleri boşluklardan ayırarak bir listeye dönüştür
    kelimeler = metin.split()

    # Kelimeleri saymak için bir sözlük oluştur
    kelime_sayilari = {}

    for kelime in kelimeler:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1
        else:
            kelime_sayilari[kelime] = 1

    # Sonuçları göster
    for kelime, sayi in kelime_sayilari.items():
        print(f"'{kelime}' kelimesi {sayi} kez geçti.")

# Ana program
metin = input("Kelime sayacı için bir metin girin: ")
kelime_sayaci(metin)
