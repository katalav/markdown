# PYTEST-TESTAUSFUNKTIOT (PYTEST testin nimi)
# =================

# MODULIRN JA KIRJASTOJEJ LATAUKSET
# ----------------------------------

# Käyttöjärjestelmän virheilmoitusten testaus vaatii pytest:n lataamisen
import pytest
# Ladataan testattava moduli 

import periytyminen

# Luodaan testiolioita eri luokista testausta varten

person = periytyminen.Person('Assi', 'Kalma') #periytyminen laitetaan jotta löydetään se toisesta kansiosta 
student = periytyminen.RasekoStudent('Jonne', 'Jantteri', '45678')

teacher = periytyminen.RasekoTeacher('Mikko', 'Viljanen',['TiVi20oa','TiVi20ka', 'TiVi22'])


# TESTAUSFUNKTIOT ELI YKSIKKÖTESTIT
#================

def test_person_properties():
    assert person.givenName == 'Assi'
    assert person.surName == 'Kalma'
    
    
def test_person_age3():
    assert round(person.calculateAge3('2008-12-31')) == 16
    
def test_student_properties():
    assert student.studentNumber == '45678'
