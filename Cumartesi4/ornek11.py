def listele(k, l):
    l = []
    k = []
    sayilar.sort()
    enb = 0
    for i in sayilar:
        if i > enb:
            l.append(i)
        if i < enb:
            k.append(i)
            k.sort(reverse=True)
    print(l)
    print(k)
    return k, l

sayilar = [2,6,1,8,7,34,1,3,6,12,23]
listele(sayilar)

#BİTMEDİ