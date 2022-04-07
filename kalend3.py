import calendar
from calendar import monthrange
from datetime import datetime, date
def date_check2():
    with open("test.txt", "r", encoding="utf-8") as file:
        f = file.read()
        f1 = f.split('/')
    if len(f1) == 1 :
        year = int(f1[-1])
        if calendar.isleap(year) == True:
            print("Rok ktory podales jest przestepny")
        else:
            print("Rok ktory podales nie jest przestepny ")
    elif len(f1) == 2 :
        year = int(f1[-1])
        month = int(f1[-2])
        if calendar.isleap(year) == True:
            print("Rok ktory podales jest przestepny")
        else:
            print("Rok ktory podales nie jest przestepny ")
        f1 = monthrange(year, month)
        print("Miesiac ktory podales ma ", f1[-1], "dni")
    elif len(f1) == 3 :
        year = int(f1[-1])
        month = int(f1[-2])
        day = int(f1[0])
        if calendar.isleap(year) == True:
            print("Rok ktory podales jest przestepny")
        else:
            print("Rok ktory podales nie jest przestepny ")
        f1 = monthrange(year, month)
        print("Miesiac ktory podales ma ", f1[-1], "dni")
        day_of_year = date(year, month, day).timetuple().tm_yday
        print("Dzien roku: ", day_of_year)

date_check2()
