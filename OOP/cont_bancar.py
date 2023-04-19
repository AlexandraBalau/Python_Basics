class cont_bancar:
    #constructor
    def __init__(self, titular_cont, iban):
        #atribute/fields
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 0000
        self.incercari_activare = 0

    def interogare_sold(self):
        print(f'Titular {self.titular_cont}')
        print(f'IBAN {self.iban}')
        print(f'Activ {self.activ}')
        print(f'Sold {self.sold}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('------------------------------------------')

    def activare_cont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('PIN gresit')
            #self.incercari_activare = self.incercari_activare + 1
            self.incercari_activare += 1

    def alimentare_cont(self, suma):
        self.sold += suma
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {self.sold}')

    def plata_card(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')

    def salut(self):
        print(f'Buna {self.titular_cont}')

