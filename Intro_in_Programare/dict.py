lista_goala = []
dict_gol = {}

#declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Ana': 7, 'Ada': 5}

#adaugam elemente
note_elevi['Sebi'] = 7

#printam dict
print(note_elevi)

#aflam note
print(note_elevi['Gigel'])

#actualizam valori
note_elevi['Ada'] = 10
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

#stergem valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'Nu mai exista acest elev'))
print(note_elevi)

#returneaza numai cheile
print(note_elevi.keys())

