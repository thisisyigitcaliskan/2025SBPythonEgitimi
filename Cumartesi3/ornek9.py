import random

sayi = random.randint(1,100)
tahmin = 0
hak = 4

while sayi != tahmin:
    tahmin = int(input("Lütfen bir sayı giriniz: "))
    if sayi == tahmin:
        print("Tebrikler! Sayıyı bildiniz!")
        break
    if hak == 0:
        print("Kaybettiniz. Sayı:", sayi)
        break
    elif sayi > tahmin:
        print("Lütfen daha büyük bir sayı deneyiniz.")
        hak = hak - 1
    else:
        print("Lütfen daha küçük bir sayı deneyiniz.")
        hak = hak - 1