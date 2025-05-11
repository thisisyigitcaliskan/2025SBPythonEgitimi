kullaniciadi = "root"
sifre = "gizlisifre"

k_veri = input("Kullanıcı adı giriniz: ")

if k_veri == kullaniciadi:
    s_veri = input("Şifreyi giriniz: ")
    if s_veri == sifre:
        print("Giriş başarılı!")
    else:
        print("Şifreniz hatalı.")
else:
    print("Kullanıcı adı mevcut değil.")