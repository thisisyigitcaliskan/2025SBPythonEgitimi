win = +1
lose = -0.35
puan1 = 0
puan2 = 0

kazan = int(input("Kazanılan savaşları giriniz: "))
kayip = int(input("Kaybedilen savaşları giriniz: "))

puan1 = win * kazan
puan2 = lose * kayip

sonuc = puan1 + puan2 

print(sonuc)