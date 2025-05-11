hak = 3
sifre = 1234

while hak > 0:
    hak -= 1
    mesaj = int(input("Şifrenizi giriniz:"))
    if mesaj == sifre:
        print("Başarılı!")
        break
    else:
        print("Şifre yankış. Tekrar deneyiniz.")
    if hak == 0:
        print("Sistemden atıldınız.")
