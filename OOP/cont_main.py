from OOP.cont_bancar import cont_bancar

cont1 = cont_bancar('AB', 'RO001')
cont2 = cont_bancar('BB', 'RO002')

cont1.activare_cont(7777)
cont1.activare_cont(2222)
cont1.activare_cont(0000)
cont2.activare_cont(0000)

cont1.alimentare_cont(300)
cont2.alimentare_cont(700)
cont2.alimentare_cont(300)

cont1.plata_card(500)
cont1.plata_card(300)

cont1.interogare_sold()
cont2.interogare_sold()




