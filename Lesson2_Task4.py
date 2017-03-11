def is_year_leap(year):
    if (year % 4 == 0 and year %100  != 0) or year % 400 == 0:
        print("Year is leap")
    else:
        print("Year is not leap")

is_year_leap(2016)