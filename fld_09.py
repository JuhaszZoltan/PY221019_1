fogy:float = float(input('mennyit eszik az autó 100on? '))
ut:int = int(input('hány Km-t akartok megtenni? '))
ar:int = int(input('mennyibe kerül egy liter benzin? '))
utas:int = int(input('hányan vagytok? '))

print(f'egy főre jutó utiköltség: {round(ut * fogy / 100 * ar / utas)}Ft')