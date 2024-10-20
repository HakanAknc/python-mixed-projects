# Not defteri (to-do listesi) için boş bir liste oluşturuyoruz
not_defteri = []

def not_ekle(not_metni):
    not_defteri.append(not_metni)
    print(f"'{not_metni}' notu eklendi.")

def notlari_goster():
    if not_defteri:
        print("\n--- Notlar ---")
        for i, not_metni in enumerate(not_defteri, 1):
            print(f"{i}. {not_metni}")
    else:
        print("Not defteri boş.")

def not_sil(sira_no):
    if 0 < sira_no <= len(not_defteri):
        silinen_not = not_defteri.pop(sira_no - 1)
        print(f"'{silinen_not}' notu silindi.")
    else:
        print("Geçersiz sıra numarası.")

# Ana program döngüsü
while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1. Not ekle")
    print("2. Notları listele")
    print("3. Not sil")
    print("4. Çıkış")

    secim = input("Seçiminizi yapın (1-4): ")

    if secim == '1':
        not_metni = input("Eklemek istediğiniz notu girin: ")
        not_ekle(not_metni)
    elif secim == '2':
        notlari_goster()
    elif secim == '3':
        notlari_goster()
        try:
            sira_no = int(input("Silmek istediğiniz notun sıra numarasını girin: "))
            not_sil(sira_no)
        except ValueError:
            print("Lütfen geçerli bir sıra numarası girin.")
    elif secim == '4':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen 1 ile 4 arasında bir sayı girin.")
