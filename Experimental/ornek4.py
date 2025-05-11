class Ogrenci:
    def __init__(self, isim: str, ogrenciNotu: float):
        self.__isim = isim
        self.__ogrenciNotu = ogrenciNotu
    
    def notSoyle(self) -> float:
        return self.__ogrenciNotu
    
    def isimSoyle(self) -> str:
        return self.__isim

    def notuDegistir(self, yeniNot: float = 0):
        if yeniNot >= 0 and 100 >= yeniNot:
            self.__ogrenciNotu = yeniNot

    def isimDegistir(self, yeniAd: str):
        if len(yeniAd) >= 3 and len(yeniAd) <= 8:
            self.__isim = yeniAd
        else:
            print(f"Yeni isim hatalıdır: {yeniAd}")

ogrenci1 = Ogrenci("Boran", 49)

ogrenci1.isimDegistir("Mehmet")
print(ogrenci1.isimSoyle())
ogrenci1.notuDegistir(105)

print(ogrenci1.notSoyle())