# MUUTTUJAT MERKKIJONOSSA
# *************************

# Samakirjat
henkilo1 = {"etunimi": "tiina", "ika": 27}
henkilo2 = {"etunimi": "jaana", "ika": 44}
henkilo3 = {"etunimi": "iida", "ika": 7}

# perinteinen ratkaisu
print(henkilo1['etunimi']+'n', 'ikä on', henkilo1['ika'], 'vuotta')

# Sama muotoiltuna merkkijonona (fstring)

muotoiltu_merkkijono = f'{henkilo1["etunimi"]}n ikä on{henkilo1["ika"]} vuotta'