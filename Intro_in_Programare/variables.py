#variabila = zona din memoria unui calculator care pastreaza date
#variabila = cutiuta in care punem valori

#am declarat si initializat variabila marca
#nu putem sa punem spatiu in numele variabilei
#o variabila incepe cu litera mica

marca = 'Volvo' #egal este un operator de atribuire (adica punem ceva in cutiuta marca)
model = 'XC 60'

#loosely typed = nu trebuie sa specificam tipurile variabelelor

print(f'Am cumparat o masina marca: {marca}')
print(f'Am cumparat o masina modelul: {model}')

#verificam tipul variabilei
print(type(marca))

#suprascriere/override

model = 'XC 60 Facelift'
print(f'Am cumparat o masina modelul: {model}')

nume = 'Balau'
prenume = 'Alexandra'
varsta = 27
print(prenume + ' ' + nume) #concept invechit in Python; sub forma asta, accepta doar un singur tip de variabile

#f = format string
print(f'Ma numesc {prenume} {nume} si am varsta de {varsta} ani.')