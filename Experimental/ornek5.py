class Tasit:
    def __init__(self, marka, hiz):
        self.marka = marka
        self._hiz = hiz

    def hareketEt(self):
        print(f"{self.marka} Hareket ediyor...")
    
    def frenle(self):
        print(f"{self.marka} frenliyor...")
    
class Araba(Tasit):
    def __init__(self, marka, hiz):
        super().__init__(marka, hiz)
    
    def muzikCal(self):
        print("Müzik çalınıyor...")

class Bisiklet(Tasit):
    def __init__(self, marka, hiz):
        super().__init__(marka, hiz)
    
    def zilCal(self):
        print("Zil çalındı!")

bisiklet = Bisiklet("Boran", 23)
araba = Araba("Ferrari", 999)

araba.hareketEt()
bisiklet.hareketEt()

araba.muzikCal()
bisiklet.zilCal()

araba.frenle()
bisiklet.frenle()