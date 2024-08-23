
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
    else:
        num = a;
    res = num;
    for _ in range(b):
       res *= num;
    return res;
# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working