 # LUOKAT JA OLIOT
 #------------------
 
 #OLION MALLIT ELI LUOKAT
 #***********************
 
 # KIRJASTO JA MODUULIT
 #======================
 
import datetime
 
class Student():
    """A class for student objects."""
    
    # Konstruktori-metodi eli oliomuodostin
    def __init__(self, name: str, group: str, dateOfBirth: str):
        """Constructor for a student object

        Args:
            name (str): The name of student
            group (str): His or hers class
            dateOfBirth (str): Date of birth is ISO format
        """
        # Luokan kentät, joista tulee objektien ominaisuudet
        self.name = name 
        self.group = group 
        self.birthday = dateOfBirth

    def studentOf(self) -> None:
        """Print students name and class on the console
        """
        memberInGroup = f'{self.name} opiskelee luokalla {self.group}'
        print(memberInGroup)
        
    def calculateAge(self) -> float:
        """Calculate student's correct age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(self.birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days /365
        return round(ageInYears)
  
if __name__ == "__main__":
 
        
    student = Student('Jonne', 'Auto23A', '2008-05-21')

    print(student.name, 'on syntynyt', student.birthday)

    student2 = Student('Tuittu', 'TiVi20ao', '1990-03-09')
    student2.studentOf() 
    print('ikä on', student2.calculateAge())



