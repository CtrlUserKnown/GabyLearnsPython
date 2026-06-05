"""
Object-Oriented Models Module

Defines domain models for a vehicle management and
pet adoption system using classes and inheritance.
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.make} {self.model}"


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"


class Pet(Animal):
    def __init__(self, name, sound, ownerName):
        super().__init__(name, sound)
        self.ownerName = ownerName

    def greetOwner(self):
        return f"{self.name} runs to {self.ownerName}!"


myPet = Pet("Buddy", "Woof", "Gaby")


class BankAccount:
    def __init__(self, accountHolder, balance=0):
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, accountHolder, balance=0, interestRate=0.02):
        super().__init__(accountHolder, balance)
        self.interestRate = interestRate

    def applyInterest(self):
        self.balance += self.balance * self.interestRate


myAccount = BankAccount("Gaby", 100)
myAccount.accountHolder = "Gabriela"

animalOne = Animal("Cat", "Meow")
animalTwo = Animal("Dog", "Woof")
animalOne.name = "Kitty"
