import calendar
from calendar import monthrange
from datetime import datetime, date

def date_check1():
    inputdate = input("Podaj date w formacie 'dd/mm/yyyy' : ")
    x = inputdate.split('/')
    if len(x) == 1:
        year = int(x[-1])
        if calendar.isleap(year) == True:
            print("Rok ktory podales jest przestepny")
        else:
            print("Rok ktory podales nie jest przestepny ")
    elif len(x) == 2:
        year = int(x[-1])
        month = int(x[-2])
        if calendar.isleap(year) == True:
            print("Rok ktory podales jest przestepny")
        else:
            print("Rok ktory podales nie jest przestepny ")
        x = monthrange(year, month)
        print("Miesiac ktory podales ma ", x[-1], "dni")
    elif len(x) == 3:
        year = int(x[-1])
        month = int(x[-2])
        day = int(x[0])
        if calendar.isleap(year) == True:
            print("Rok ktory podales jest przestepny")
        else:
            print("Rok ktory podales nie jest przestepny ")
        x = monthrange(year, month)
        print("Miesiac ktory podales ma ", x[-1], "dni")
        day_of_year = date(year, month, day).timetuple().tm_yday
        print("Dzien roku: ", day_of_year)
date_check1()