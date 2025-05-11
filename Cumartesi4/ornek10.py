def listele(l):
    l = []
    sayilar.sort()
    enb = 0
    for i in sayilar:
        if i > enb:
            l.append(i)
    print(l)
    return l

sayilar = [2,6,1,8,7,34,1,3,6,12,23]
listele(sayilar)