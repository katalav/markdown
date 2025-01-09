import datetime
from dateutil.relativedelta import relativedelta

def calculateAge(year, month, day):
    
        birthDate = datetime.datetime(year, month, day)
        today = datetime.datetime.today()
    
        ageDelta = relativedelta(today, birthDate)
        
        return f"{ageDelta.years} vuotta"
    
    
    #päivämäärien kanssa joudutaan aina tappelemaan.
print(calculateAge( 1990, 1, 1 ))