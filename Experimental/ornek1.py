class Sinif:
    def __init__(self, sinifsayisi, ad):  # kullanıcıdan veri almak için
        print("sınıfa hoş geldin")
        self.sinifsayisi = sinifsayisi
        self.ad = ad
        self.gizli = "selam" # burada kullanıcıdan veri almaya gerek olmadığı için böyle kullandık

    def DersPrograminigoster(self):
        print(self.ad)
        print("pazartesi - matematik, türkçe, blablabla")
        print("sali - türkçe, matematik, blabka")
        print("...")
        print(end="\n\n\n")

    def __str__(self):
        return ("Biz {} sınıfıyız ve toplam {} kişiyiz.".format(self.ad, self.sinifsayisi))


sinifA = Sinif(20, "A sınıfı")
sinifB = Sinif(20, "B sınıfı")

print(sinifA)
print(sinifB)