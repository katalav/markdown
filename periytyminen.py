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
    
    def __init__(self, givenname: str, surname: str):
        """Creates a Person object

        Args:
            givenname (str): A first name
            surname (str): A last name
        """
        self.givenName = givenname
        self.surName = surname
        
    def calculateAge3(self, isoBirthday: str) -> float:#(perinteinen tapa tehdä)
        birthday = datetime.datetime.fromisoformat(isoBirthday)
        age = datetime.datetime.now() - birthday
        ageInYears = age.days / 365
        return ageInYears
        
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
    def __init__(self, givenName: str, surName: str, studentNumber: str):
        """Creates a student object

        Args:
            givenName (str): Student's first name
            surName (str): Student's last name
            studentNumber (str): Student's (student number) ID
        """
        super().__init__(givenName, surName) # Määritellääm tapahtuvaksi yliluokan mukaan
        self.studentNumber = studentNumber # Ei määritelty yliluokassa
        
class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name of the super class
    """
    def __init__(self, givenName: str, surName: str, groups: list[str]):
        """Constructor method for Teacher objects

        Args:
            givenName (str): Techer's given name
            surName (str): Teacher's surname
            groups (list[str]): List of student groups
        """
        super().__init__(givenName, surName)
        self.groups = groups
       

    
        
if __name__ == "__main__":
    rasekoStudent = RasekoStudent('Jonne', 'Jantteri','456343')
    print(rasekoStudent.givenName)

    
    groups = ['Tivi23A', 'TiVi23B', 'TiVi20ao']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', 'TiVi23A')
    
    print(f'{rasekoTeacher.givenName} opettaa ryhmiä {rasekoTeacher.groups}')
    
    # Luodaan moduulista oliot.py Student.olio
    student = Student('Tuittu Kiukkunen', 'Auto22B', '2007-10-23')
    print(f'{student.name} on{student.calculateAge()}')
    
    
    ika = Person.calculateAge('2008-03-22')
    print(ika)
    
    ika2 = Person.calculateAge2('1978-12-10')
    print(ika2)

    person1 = Person('Calle', 'Keckerberg')
    ika3 = person1.calculateAge3('2009-10-22')
    print(f'Henkilön {person1.givenName} ikä on {ika3} vuotta') 