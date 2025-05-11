sayi = int(input("Bir sayı girin: "))

for i in range(1, sayi + 1):
    bosluk = " " * (sayi - i)
    yildiz = "*" * (2 * i - 1) 
    print(bosluk + yildiz)