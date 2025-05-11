sinav1 = int(input("1. Sınav: "))
sinav2 = int(input("2. Sınav: "))
performans = int(input("Performans: "))

sonuc1 = sinav1 * 30 / 100
sonuc2 = sinav2 * 50 / 100
sonuc3 = performans * 20 / 100

genel = sonuc1 + sonuc2 + sonuc3
print(genel)

genel > 70 == print("Geçti")
genel <= 70 == print("Kaldı")