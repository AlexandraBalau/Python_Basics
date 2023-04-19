#listele in python pot sa cuprinda elemente de tipuri diferite
#au dimensiune dinamica

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

#afisam lista
print(fructe)

#accesam un element in functie de index
print(fructe[2])

#adaugam un nou element
fructe.append('rosie')

#suprascriem un element
fructe[0] = 'para'
print(fructe)

#aflam dimensiunea
print(len(fructe))

#scoate si ne returneaza ultimul element
last = fructe.pop() #scoate ultimul element, dar il retine in memorie
print('ultimul elem:', last)
print('lista:', fructe)

#de cate ori apare un element in lista
print(fructe.count(3))

#extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)
