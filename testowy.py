import calendar
from calendar import monthrange
from datetime import datetime, date
def test1(*args):
    for x in args:
        y = x.split('/')
        if len(y) == 1 :
            year = int(y[-1])
            if calendar.isleap(year) == True:
                print("Rok ktory podales jest przestepny")
            else:
                print("Rok ktory podales nie jest przestepny ")
        elif len(y) == 2:
            year = int(y[-1])
            month = int(y[-2])
            if calendar.isleap(year) == True:
                print("Rok ktory podales jest przestepnyyy")
            else:
                print("Rok ktory podales nie jest przestepnyyyy ")
            y = monthrange(year, month)
            print("Miesiac ktory podales ma ", y[-1], "dni")
        elif len(y) == 3:
            year = int(y[-1])
            month = int(y[-2])
            day = int(y[0])
            if calendar.isleap(year) == True:
                print("Rok ktory podales jest przestepny")
            else:
                print("Rok ktory podales nie jest przestepny ")
            y = monthrange(year, month)
            print("Miesiac ktory podales ma ", y[-1], "dni")
            day_of_year = date(year, month, day).timetuple().tm_yday
            print("Dzien roku: ", day_of_year)



test1("01/01/2020")
