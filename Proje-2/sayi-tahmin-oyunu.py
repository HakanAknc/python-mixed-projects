"""
Bu proje, kullanıcının belirli bir aralıkta rastgele oluşturulan bir sayıyı tahmin etmesi gereken bir oyun oluşturmayı içerir. Program, kullanıcının tahminlerini daraltmalarına yardımcı olacak geri bildirimler sağlar. 
"""
import random
import time

user_input_min = int(input("Aralığın minimum sayısını giriniz: "))
user_input_max = int(input("Aralığın maximum sayısını giriniz: "))

random_number = random.randint(user_input_min, user_input_max)

count = 0
user_numbers = []

while True:
    user_guess = int(input("Aradaki sayıyı tahmin edin {} ve {}: ".format(user_input_min, user_input_max)))

    if user_guess == random_number:
        count += 1
        user_numbers = []
        if count == 1:
            print("Harikasın! Sayıyı tahmin ettiniz {} deneme ^_^ Numarası şuydu: {}".format(count, random_number))
        else:
            print("Harikasın! Sayıyı tahmin ettiniz {} çalışır ^_^ Numarası şuydu: {}".format(count, random_number))
        time.sleep(1)
        play_again = input("Tekrar oynamak ister misin? (E/H): ")
        if play_again.lower() == "e":
            user_input_min = int(input("Aralığın minimum sayısını girin: "))
            user_input_max = int(input("Aralığın maksimum sayısıını giriniz: "))
            random_number = random.randint(user_input_min, user_input_max)
            count = 0
            user_numbers = []
            continue
        else:
            time.sleep(1)
            print("Tamam, iyi günler!")
            break
    elif user_guess < random_number:
        user_numbers.append(user_guess)
        user_numbers.sort()
        count += 1
        print("Sayı tahmininizden daha yüksek.")
        print("Önceki tahminleriniz: {}".format(user_numbers))
        time.sleep(1)
    elif user_guess > random_number:
        user_numbers.append(user_guess)
        user_numbers.sort()
        count += 1
        print("Sayı tahmininizden düşük")
        print("Önceki tahminleriniz: {}".format(user_numbers))
        time.sleep(1)