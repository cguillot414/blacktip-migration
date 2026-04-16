#By CM Guillot Fall 2025
#day of the year


def DOY(month = 'jan', day = 0, year = 0):
    
    month = month.lower()
    if((day > 31) | (day < 0)):
        raise OverflowError("Invalid day")
    if(year < 0):
        raise OverflowError("Invalid year")
    if(len(month) > 3):
        raise OverflowError("Invalid month. Try first 3 digits")
    
    doy = day;
    
    if(month == "jan"):
        if(day <= 31):
            return doy
    doy += 31
    if(month == "feb"):
        if(day <= 29):
            return doy
    doy += 28
    if(year % 4 == 0): #leap year
        doy += 1
    if(month == "mar"):
        if(day <= 31):
            return doy
    doy += 31
    if(month == "apr"):
        if(day <= 30):
           return doy
    doy += 30
    if(month == "may"):
        if(day <= 31):
            return doy
    doy += 31
    if(month == "jun"):
        if(day <= 30):
           return doy
    doy += 30
    if(month == "jul"):
        if(day <= 31):
           return doy
    doy += 31
    if(month == "aug"):
        if(day <= 31):
            return doy
    doy += 31
    if(month == "sep"):
        if(day <= 30):
           return doy
    doy += 30
    if(month == "oct"):
        if(day <= 31):
            return doy
    doy += 31
    if(month == "nov"):
        if(day <= 30):
           return doy
    doy += 30
    if(month == "dec"):
        if(day <= 31):
            return doy
    
    raise OverflowError("Invalid date")
    



    