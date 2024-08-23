import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a: int, b: int) -> float:
    res: float = 0;
    if b == 0:
        return 1;
    elif b < 0:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero!");
        else:
            num: float = 1 / a;
            b *= -1;
    else:
        num = a;

    res = num;
    for _ in range(b-1):
       res *= num;

    return res;

def sqrt(a: int) -> float:
    return math.sqrt(a);

def is_primary(a: int) -> bool:
    if a < 2:
        return False;
    for i in range(2, a):
        if not a%i:
            return False;
    return True;

def factorial(a: int) -> int:
    if a < 0:
        raise ValueError("factorial not defined for negative values");
    elif a == 0:
        return 1;
    else:
        return a*factorial(a-1);

# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working