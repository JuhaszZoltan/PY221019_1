print('''
======árlista======
alma      350 Ft/Kg
körte    1180 Ft/Kg
szilva    500 Ft/Kg
''')

vegosszeg:float = 0
koszones:str = 'Jó napot, szeretnél valamit vásárolni? '
while input(koszones) == 'igen':
    termek = input('Mit szeretnél? ')
    if termek not in ['alma', 'körte', 'szilva']:
        print(f'Sajnos {termek} jelenleg nincs :(')
    else:
        mennyiseg = float(input(f'hány Kg {termek}t kérsz? '))
        if termek == 'alma':
            vegosszeg += (350 * mennyiseg)
        elif termek == 'körte':
            vegosszeg += (1180 * mennyiseg)
        elif termek == 'szilva':
            vegosszeg += (500 * mennyiseg)
    koszones = 'Rendben. Szeretnél még valamit vásárolni? '
print(f'Oké, osszesen {round(vegosszeg)} Ft-ot kérnék!')
print('Viszont látásra!')