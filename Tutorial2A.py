import math
#Question 1A
def calcFahrenheit(C):
    F = (1.8*C + 32)
    return F

#Question 1B
def is_coldday(C):
    if calcFahrenheit(C) < 50:
        return True
    else:
        return False

#Question 2A
def calcAngle(a,b,c):
    C = ((b**2+c**2-a**2)/(2.*b*c))
    return math.degrees(math.acos(C))
