# se ihan eka hei maailma esimerkki

print('Hello World')

print('Ja tämän sovelluksen koodisi Jantteri Jäynä')

# RAKENTEELLISET MUUTTUJAT
#-------------------------

nimilista = ["jonne", "jasmiina", "aleksi"] # lista list
print("listassa ensimmäisenä on", nimilista [0])
jasenia = len(nimilista)#listan jäsenenmäär selviää len- komennolla
print("nimilistassa on", jasenia, "henkilöä")
nimilista.sort() # järjestää listan aakkosjärjestyksessä
print("Aakkostettu lista on", nimilista)

ryhmat = ("TiVi24A", "TiVi23B", "TiVi20ao") #monikko tuple
## muista pilkut biiitch
#ryhmat [2] = "TiVi20oa" #yksittäistä jäsentä ei voi muuttaa
ryhmat = ("TiVi24A", "TiVi23B", "TiVi20ao") #koko monikon voi muuttaa
print("meidän uusiryhmä on", ryhmat[2])

joukko = {"tuittu", "assi", "cello"} #joukko set
print("Ja joukkoon kuuluvat", joukko)# huomaa järjestys
#print(joukko [2]) ei toimi, koska jäseneen ei voi viitata indeksillä

#sanakirja dictionary (dist)
henkilotiedot = {"etunimi": "jonne", "sukunimi": "jantteri" , "ika": 16}

print("opiskelijan", henkilotiedot["etunimi"], "ikä on ", henkilotiedot["ika"])

opiskelija1 = {"etunimi": "jonne", "sukunimi": "jantteri" , "ika": 16}
opiskelija2 = {"etunimi": "tuittu", "sujunimi": "kiukkunen", "ika": 27}
opiskelija3 = {"etunimi": "iina", "sukunimi": "urpo" , "ika": 17}

opiskelijalista = [opiskelija1, opiskelija2, opiskelija3]
print("opiskelijalista on", opiskelijalista)

uusi_opiskelija = {"etunimi": "Assi", "sukunimi": "Kalma" , "ika": 65}

#lisätään uusi orvo olemassa olevaan listaan
opiskelijalista.append(uusi_opiskelija)

#tulstetaan opiskelijalistan ensimmäinen jäsen
print("Listassa ensimmäinen on", opiskelijalista.pop(0))
print("ja viimeisenä on", opiskelijalista.pop())

