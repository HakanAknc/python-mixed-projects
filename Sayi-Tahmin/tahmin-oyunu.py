import random

print("Merhaba oyuna hoş geldiniz. Bu bir sayı tahmin oyunudur. \nSayıyı tahmin etmek için 7 şansınız var. Hadi oyuna başlayalım")

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Lütfen tahminizi giriniz: "))

    if my_guess == number_to_guess:
        print(f'Sayı {number_to_guess} ve doğru buldun !! {guess_counter} denemesinde')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops üzgünüm, sayı {number_to_guess} bir dahaki sefer daha iyi şanslar')

    elif my_guess > number_to_guess:
        print(f'Tahmininiz yüksek')
    
    elif my_guess < number_to_guess:
        print(f'Tahmininiz düşük')