import random

secenek = 0
toplam_b = random.randint(1000,3000)

while secenek != 4:
    print("1: Bakiye sorgulama, 2: Para yatırma, 3: Para Çekme, 4: Çıkış yap")
    secenek = int(input("Lütfen işleminizi seçiniz: "))
    if secenek == 1:
        print("Bakiyeniz: ", toplam_b)

    elif secenek == 2:
        yatirma = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        toplam_b = yatirma + toplam_b
        print(toplam_b)

    elif secenek == 3:
        cekme = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if cekme > toplam_b:
            print("Yetersiz bakiye.")
            continue
        toplam_b = toplam_b - cekme
        print(toplam_b)

    elif secenek == 4:
        print("İyi günler.")

    else:
        print("Hatalı tuşlama. 1-4 arasında seçim yapınız.")
