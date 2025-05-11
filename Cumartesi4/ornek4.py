def topla(sayi=0):
    toplam = 0
    for i in range(sayi + 1):
        toplam = i + toplam
    return toplam
x=topla(10)
print(x)