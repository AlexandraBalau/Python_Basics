def print_greeting():
    print("Buna ziua, bine ati venit!")

def print_greeting_by_name(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def media_nr(a, b, c):
    return (a + b + c)/3

def pi_value():
    return 3.14

def varsta_major(varsta):
    if varsta >= 18:
        return True
    else:
        return False

#zona de apelare
print_greeting()
print_greeting()
print_greeting_by_name('Balau', 'Alexandra')
print(media_nr(3, 3, 4))
print(pi_value())
print(varsta_major(18))

#se ia varsta utilizatorului
age = int(input("Introduceti varsta dvs: "))
if varsta_major(age):
    print('Cont creat. Bine ai venit in aplicatie')
else:
    print('Nu ai varsta minima necesara')

'''
oop:

variabilele => atribute/proprietati/fields
functii => metode
'''

