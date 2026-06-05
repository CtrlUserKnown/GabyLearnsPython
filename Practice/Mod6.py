"""
Payment and File Processing Module

Demonstrates error handling patterns for payment validation,
data conversion, and file operations.
"""

try:
    result1 = 10 / 0
except ZeroDivisionError:
    result1 = "cannot divide by zero"

try:
    result2 = int("hello")
except ValueError:
    result2 = "cannot convert to int"

shortList = [1, 2, 3]
try:
    result3 = shortList[10]
except IndexError:
    result3 = "index out of range"

try:
    divResult = 10 / 2
except ZeroDivisionError:
    divResult = None
else:
    divResult = divResult

finallyRan = None
try:
    1 / 1
except ZeroDivisionError:
    pass
finally:
    finallyRan = "finally ran"


def getElement(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None


def validateAge(age):
    if age < 0:
        raise ValueError("Age cannot be negative")


try:
    result7 = validateAge(-1)
except ValueError:
    result7 = "caught ValueError"


def safeDivide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


try:
    result9 = "hello" + 5
except TypeError:
    result9 = "caught TypeError"


def checkStock(quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    if quantity == 0:
        raise Exception("Out of stock.")
    return "In stock"


try:
    parsedFloat = float("3.14")
except ValueError:
    parsedFloat = None
else:
    parsedFloat = parsedFloat
finally:
    inputCheckDone = "done"


def openFile():
    try:
        f = open("data.txt")
        f.close()
        return "file found"
    except FileNotFoundError:
        return "file not found"
