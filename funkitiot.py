# FUNKTIOT
#==============

#Funktio, joka ei palauta arvoa eikä käytä argumetteja

def tervehdys():
    """Prints Hyvää Huomenta on the screen
    """
    print('Hyvää huomenta!')
    
tervehdys()
    
def toivotus(nimi, aika):
    """Greets user differently accorting to the time of day

    Args:
        nimi (str): user's name
        aika (int): hour in millitary format
    """
    if aika > 16:
        viesti = f'Hyvää iltaa {nimi}'
    elif aika > 10:
        viesti = f'Hyvää päivää {nimi}'
    else:
        viesti = f'Hyvää huomenta {nimi}'
        
    print(viesti)
        
toivotus( 'Mika', 9)
  
alkuLitania = 'Milloin minä olisin työt tehnyt'   
def tyoMotivaatio(paiva: str) -> str:
    """Return the motto of working of day in Finnish

    Args:
        paiva (str): Weekday name in Finnish

    Returns:
        str: The motto of the day
    """
    mottoDictionary = {'Maanantai': 'na en malttanut',
             'Tiistai': 'na en tietänyt',
             'Keskiviikko' : 'na en kerennyt',
             'Torstai': 'na en tohtinut',
             'Perjantai': 'na on paha päivä',
             'Lauantai': 'on pyhän aatto',
             'Sunnuntai': 'suuri juhla'}
    
    dailyMotto = f'{alkuLitania} {paiva.capitalize()}{mottoDictionary[paiva]}.'
    return dailyMotto

print(tyoMotivaatio('Torstai'))

