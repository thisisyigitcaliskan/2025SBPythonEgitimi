# indexler 0         1       2
names = ["Yağmur", "Enes", "Ekim"]

# print(type(names))

# print(names)
# print(names[1]) # sayiların istenilen indexteki elemanı yazdırma

# if "Yağmur" in names:
#     print("var")

# listenin boyutu
# print(len(names))
# print(len("Yağiz"))

# listenin sonuna eleman ekleme
names.append("Eylül")
# print(names)

# değer silme
names.remove("Eylül")
# print(names)

# araya değer ekleme
names.insert(2, "Boran")
# print(names)

# indexe göre silme
# print(names)
isim = names.pop(3) # sildiğimiz değeri isim adlı değşkene atlıyoruz
# print(names)
# print(isim)
names.remove("Boran")
# print(names)

# ters çevirme
names.reverse()
# print(names)


# sort sıralama
names1 = ["Mehmet","Yağiz","Zeynep","Ali"]
names1.sort()
# print(names1)


# uygulama 1
sayilar = [1, 2, 3, 4]
# print(sayilar)

yazdir = f"(s1:{sayilar[0]}) - (s2:{sayilar[1]}) - (s3:{sayilar[2]}) - (s4:{sayilar[3]})"
print(yazdir)

sayilar[1] = 10  # 2 sayısını 10 ile değiştiriyoruz
print(sayilar)

uzunluk = "Lisetenin Uzunluğu {}".format(len(sayilar)) # listenin uzunluğunu buluyoruz
print(uzunluk)

sayilar.append(61.67)   # listenin son sırasına eleman ekliyoruz
print(sayilar)

sayilar.insert(2,1000) # listenin 2. ve 3. elemanı arasısa eleman ekleme
print(sayilar)

sayilar.remove(61.67)  # istenilen değerdeki elemanı silme
print(sayilar)

sayilar.pop()  # listenin son elemanını silme
print(sayilar)

sayilar.sort()  # sıralama
print(sayilar)

sayilar.reverse()  # ters çevirme
print(sayilar)

