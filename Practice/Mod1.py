"""
City Information Configuration Module

Manages city data, measurements, pricing, and user interaction
utilities for the city information system.
"""

cityName = "New York"

length = 50
width = 30
area = length * width

temperature = 98.6


def greetUser():
    print("Welcome to the city information system!")


def addNumbers(a, b):
    return a + b


total = addNumbers(15, 27)


def squareNumber(number):
    return number * number


price = 49.99
quantity = 3
orderCost = price * quantity


def convertToMeters(feet):
    return feet * 0.3048


def getFullName(firstName, lastName):
    return firstName + " " + lastName


score = 0


def addPoints(number):
    global score
    return score + number
