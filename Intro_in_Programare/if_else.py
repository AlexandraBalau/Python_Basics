piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

#daca nr este par printam acest lucru, altfel printam impar
nr = 4
if nr % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")

#este numar pozitiv?

if nr > 0:
    print("pozitiv")
else:
    print("nu este pozitiv")

#if, else if, else
#cum ne saluta robotelul, in fucntie de ora?

#luam date de la tastatura input()
#ne asiguram ca sunt transformate din str in int int()
# ora = int(input('Introdu ora: '))
# if ora < 0:
#     print('ora invalida. ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')
# CTRL + / => comentam/decomentam liniile de cod

optiunea = int(input('Alege o optiune: '))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales ro')
elif optiunea == 2:
    print('ati ales en')
else:
    print('nu am identificat optiunea, mai incearca')