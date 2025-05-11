def ucgen(sayi):
    for i in range(1, sayi + 1):
        bosluk = " " * (sayi - i)
        yildiz = "*" * (2 * i - 1) 
        print(bosluk + yildiz)
    return sayi

ucgen(5)

