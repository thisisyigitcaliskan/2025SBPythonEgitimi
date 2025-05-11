import random

kisi_sayisi = int(input("Lütfen kişi sayılarını giriniz: "))
isimler = list()

sayac = 0
while sayac < kisi_sayisi:
    sayac = sayac + 1
    isim = input(f"{sayac}. Kişini adını gir: ")
    isimler.append(isim)

print(random.choice(isimler))

