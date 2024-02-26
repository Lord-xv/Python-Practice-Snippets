#2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 

def is_leap(year):
    leap = False
    
    a = year % 4
    b = year % 100
    c = year % 400

    x = (not bool(a)) * bool(b)
    y = (not bool(b)) * bool(c)

    if bool(x):
        leap = True
    elif  bool(y):
        leap = False
    else :
        leap = (not bool(a))
    
    print(a)
    print(b)
    print(c)
    return leap

year = int(input())
print(is_leap(year))


