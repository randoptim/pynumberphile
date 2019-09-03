# https://www.youtube.com/watch?v=azL5ehbw_24
from sympy import isprime

def LeftExtensionsOfPrime(n):
    print n
    for i in range(1, 10):
        if isprime(int(str(i)+str(n))):
            LeftExtensionsOfPrime(int(str(i)+str(n)))
    
def RightExtensionsOfPrime(n):
    print n
    for i in range(1, 10):
        if isprime(int(str(n)+str(i))):
            RightExtensionsOfPrime(int(str(n)+str(i)))

def IsLeftTruncatablePrime(n):
    if isprime(n) and ((n < 10) or (n > 10 and IsLeftTruncatablePrime(int(str(n)[1:])) )):
        return True
    return False

def IsRightTruncatablePrime(n):
    if isprime(n) and ((n < 10) or (n > 10 and IsRightTruncatablePrime(int(str(n)[:-1])) )):
        return True
    return False

def IsDeletablePrime(n):
    if n < 10:
        if isprime(n):
            return True
        return False
    for i in range(0, len(str(n))):
        if IsDeletablePrime(int(str(n)[0:i]+str(n)[i+1:])):
            return True
    return False   
