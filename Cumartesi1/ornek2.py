# x = range(1,10)
# print(list(x))

# print("döngü başladi")
# for sayi in range(1,10):
#     print(sayi)

# for a in range(0,21,2):
#     print(a)

# print("\nyada\n")

# for a in range(0,21):
#     if a % 2 == 0:
#         print(a)

# for a in range(0,21):
#     if a % 2 == 1:
#         print("tek")

# for karakter in "python":
#     print(karakter)

# uygulama 1 kullanıcının girdiği sayıya kadar olan sayıları toplayıp ekrana yazdır

toplam = 0
s1 = int(input("s1: "))
s2 = int(input("s2: "))
for x in range(s1,s2+1):
    toplam += x
print(toplam)
