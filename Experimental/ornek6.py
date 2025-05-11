class Calculator:
    def __init__(self):
        self.sayi1 = float(input("1. Sayıyı giriniz: "))
        self.sayi2 = float(input("2. Sayıyı giriniz: "))
        print("1: Toplama, 2: Çıkarma, 3: Bölme, 4: Çarpma, 0: Çıkış Yap")
        self.islem = int(input("Yapmak istediğiniz işlemi seçiniz: "))

    def toplama(self):
            sonuc = self.sayi1 + self.sayi2
            print(sonuc)
    
    def cikarma(self):    
            sonuc = self.sayi1 - self.sayi2
            print(sonuc)
        
    def bolme(self):
            sonuc = self.sayi1 / self.sayi2
            print(sonuc)
        
    def carpma(self):      
            sonuc = self.sayi1 * self.sayi2
            print(sonuc)

    def calistir(self):
        if self.islem == 1:
            self.toplama()
        if self.islem == 2:
            self.cikarma()
        if self.islem == 3:
            self.bolme()
        if self.islem == 4:
            self.carpma()

calc = Calculator()
calc.calistir()