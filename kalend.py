import calendar
from calendar import monthrange
from datetime import datetime, date

def time1(year,month = 0,day = 0):
    if calendar.isleap(year) == True:
        print("Rok ktory podales jest przestepny")
    else:
        print("Rok ktory podales nie jest przestepny ")
    if month > 0:
         y = monthrange(year,month)
         print("Miesiac ktory podales ma ", y[-1], "dni")
    else :
        pass
    if day > 0:
        day_of_year = date(year, month, day).timetuple().tm_yday
        print("Dzien roku: ", day_of_year)
    else:
        pass
time1(2000,12,31)