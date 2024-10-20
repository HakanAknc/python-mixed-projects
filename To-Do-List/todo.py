yapılacaklar_listesi = []

def gorev_ekle(gorev):
    yapılacaklar_listesi.append(gorev)
    print(f"Görev eklendi: {gorev}")

def gorevleri_listele():
    if len(yapılacaklar_listesi) == 0:
        print("Henüz yapılcak görev eklenmedi.")
    else:
        print("Yapılacaklar listesi: ")
        for i, gorev in enumerate(yapılacaklar_listesi, 1):
            print(f"{i}. {gorev}")

def gorev_sil(gorev_numarasi):
    if gorev_numarasi > len(yapılacaklar_listesi) or (gorev_numarasi) <= 0:
        print("Geçersiz görev numarası")
    else:
        silinen_gorev = yapılacaklar_listesi.pop(gorev_numarasi - 1)
        print(f"Görev silindi: {silinen_gorev}")

while True:
    print("\n***Yapılacaklar Listesi Uygulaması***")
    print("\n1. Görev Ekle")
    print("\n2. Görevleri Listele")
    print("\n3. Görev Sil")
    print("\n4. Çıkış")

    secim = input("Bir seçenek girin (1/2/3): ")

    if secim == "1":
        yeni_gorev = input("Eklemek istediğiniz görevi yazınız: ")
        gorev_ekle(yeni_gorev)
    elif secim == "2":
        gorevleri_listele()
    elif secim == "3":
        gorevleri_listele()
        silinecek_gorev = int(input("Silmek istediğiniz görev numarasını girin: "))
        gorev_sil(silinecek_gorev)
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Gecersiz secim, lütfen tekrar deneyin.")
