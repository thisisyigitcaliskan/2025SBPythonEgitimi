matris = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12], 
          [13, 14, 15, 16]]

toplam = 0
index = 0

while index < len(matris):
    toplam += matris[index][index]
    index += 1

print(toplam)