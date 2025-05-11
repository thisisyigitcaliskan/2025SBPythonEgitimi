class Kedi:
    def __init__(self, ad, yas):  # kullanıcıdan veri almak için
        print("sınıfa hoş geldin")
        self.ad = ad
        self.yas = yas

    def sesCikar(self):
        print(self.ad)
        print(self.yas)
        print("Çıkardım!")

    def yemekYe(self):
        print(self.ad)
        print(self.yas)
        print("Yedim!")

class Kopek:
    def __init__(self, ad, yas):  # kullanıcıdan veri almak için
        print("sınıfa hoş geldin")
        self.ad = ad
        self.yas = yas

    def sesCikar(self):
        print(self.ad)
        print(self.yas)
        print("Çıkardım!")

    def yemekYe(self):
        print(self.ad)
        print(self.yas)
        print("Yedim!")

a = Kedi("Kuçu", 20)
b = Kopek("miyav", 10)

a.sesCikar()
b.yemekYe()