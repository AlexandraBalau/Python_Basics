# #dalmatienii
#
# for i in range(1, 102):
#     print(f'Dalmatianul cu nr {i}')
#
# #dalmatienii din 2 in 2
#
# for i in range(1, 102, 2):
#     print(f'Dalmatianul cu nr {i}')
#
# numere = [3, 7, 10]
# #parcurgere lista cu for prin intermediul indexului
# for i in range(0, len(numere)):
#     print(f'indexul curent este {i}')
#     print(f'numarul curent este {numere[i]}')
#
# #for each
# for numar in numere:
#     print(f'Numarul curent este: {numar}')
#
# #for each - suma
# s = 0
# for numar in numere:
#     print(f'Numarul curent este: {numar}')
#     s = s + numar
# print(f'Suma este {s}')

#de cate ori apare 3
items = [3, 2, 3, 5, 2, 3, 3, 3]
count = 0
for item in items:
    if item == 3:
        count += 1
print(count)




