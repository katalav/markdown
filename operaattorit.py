#OPERAATTORIT JA VALINTATARAKENTEET
#==================================

etunimi = "jonne"
ika = 16

#oppivelvollinen jos alle 18v

if ika <18:
    print("opiskelija on oppivelvollinen")#maaalaa teksti ja paina "" jos unohdit laittaa ne heti alkuun
else:
    print("Ei oo pakkotulla kouluun")# sisennykset on pakko mennä oikein tai koodi ei toimi

henkilo1 = {"etunimi": "tiina", "ika": 27}
henkilo2 = {"etunimi": "jaana", "ika": 44}
henkilo3 = {"etunimi": "iida", "ika": 7}

#henkilö lasketaan nuorisoon 13 - 30
ika = henkilo2["ika"]
etunimi = henkilo2['etunimi']

if ika > 12 and ika <30:
    print(etunimi, "kuuluu nuorisoon")
elif ika <13:
    print(etunimi, "on lapsi")
else:
    print(etunimi, "on aikuinen")
    
# Vaihtoehtoinen ratkaisu 
if ika >= 30:
  print('Tervetuloa aikuiseksi', etunimi)
elif ika >= 13:
    print('Olet nuorisohuligaani', etunimi)
else:
    print('Olet pahainen kakara', etunimi)

# Paljon vaihtoehtoja sisältävä ehtorakenne

sisalto = {'ohjelmointi': 'Kehitysympäristö ja ohjelmointikielet', 'ohjelmistokehittäjänä toimiminen': 'projektityöskentely, tietovarastot, versiointi ja julkaisu', 'komponenttikirjasto': 'Django, Node.js, Qt ja muut kirjastot','Sulautetut järjestelmät': 'C-ohjelmointi, Arduino ja Raspberry Pi'}

while True:
  kysymys = input('Minkä tutkinnon osan sisällön haluat nähdä ? ')
  if kysymys == '':
      break
  
  try:
      vastaus = sisalto[kysymys]
  except Exception as e:
      vastaus = 'Ei semmoista tutkintoa ole olemassa'
    
  print(vastaus)


