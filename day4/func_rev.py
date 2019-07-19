
# leap years are divisble by 4 and if its divisble by 100, its also 
# divisible by 400
def is_leap_year(year):
    return (year % 4 == 0) 

print(is_leap_year(1600))
