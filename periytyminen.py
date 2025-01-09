# PERIYTYMINEN INHERITANCE
# =========================

# KIRJASTOT JA MODUULIT
#-----------------------
#import oliot # Tuodaan koko oliot.py sisältö
import datetime
from oliot import Student # Tuodaan oliot moduulista Student-luokka

#YLILUOKAN ELI ÄITILUOKKA (SUPER / PARENT CLASS)
#-----------------------------------------------
class Person():
    """common class for all persons in Raseko"""
    
    def __init__(self, etunimi: str, sukunimi: str):
        """Creates a Person object

        Args:
            etunimi (str): A first name
            sukunimi (str): A last name
        """
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        # Staattinen metodi, joka laskee iän. Staattisessa metodissa ei luoda oliota lainkaan
        #vaan metodia voi käyttää suoraan luokasta käsin
    @staticmethod
    def calculateAge(birthDay) -> float:
        """Calculates student's corrent age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthDay)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)
        pass
    # Luokkametodi on myös staattinen, eli ei vaadi olion muodostamista
    # Huomaa luokkaan viittaava cls, joka korvaa perinteisen self:n
    @classmethod
    def calculateAge2(cls, birthday):
        """Calculates student's corrent age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)
    

# ALILUOKKA ELI LAPSILUOKKA (SUB / CHILD CLASS)
#----------------------------------------------
class RasekoStudent(Person):
    """The student class, inherits The Person class"""
    def __init__(self, etunimi: str, sukunimi: str, opiskelijanumero: str):
        """Creates a student object

        Args:
            etunimi (str): Opiskelijan etunimi
            sukunimi (str): Opiskelijan sukunimi
            opiskelijanumero (str): Opiskelija numero
        """
        super().__init__(etunimi, sukunimi) # Määritellääm tapahtuvaksi yliluokan mukaan
        self.opiskelijanumero = opiskelijanumero # Ei määritelty yliluokassa
        
class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name of the super class
    """
    def __init__(self, etunimi: str, sukunimi: str, luokat: list[str]):
        """Constructor method for Teacher objects

        Args:
            etunimi (str): Techer's given name
            sukunimi (str): Teacher's surname
            luokat (list[str]): List of student groups
        """
        super().__init__(etunimi, sukunimi)
        self.luokat = luokat
       

    
        
if __name__ == "__main__":
    rasekoStudent = RasekoStudent ('Jonne', 'Jantteri','456343')
    print(rasekoStudent.sukunimi)

    
    luokat = ['Tivi23A', 'TiVi23B', 'TiVi20ao']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', luokat)
    
    print(f'{rasekoTeacher.etunimi} opettaa ryhmiä {rasekoTeacher.luokat}')
    
    # Luodaan moduulista oliot.py Student.olio
    student = Student('Tuittu Kiukkunen', 'Auto22B', '2007-10-23')
    print(f'{student.name} on{student.calculateAge()}')
    
    
    ika = Person.calculateAge('2008-03-22')
    print(ika)
    
ika2 = Person.calculateAge2('1978-12-10')
print(ika2)