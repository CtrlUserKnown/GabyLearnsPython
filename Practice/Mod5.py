"""
Data Processing Module

Collection of data processing utilities for working with
lists, loops, and data transformations.
"""

animals = ["cat", "dog", "bird", "fish", "hamster"]
printedAnimals = []
for a in animals:
    printedAnimals.append(a)

oneToTen = []
for i in range(1, 11):
    oneToTen.append(i)

countUp = []
i = 1
while i <= 5:
    countUp.append(i)
    i += 1

prices = [1.99, 2.50, 3.75, 4.00]
priceTotal = 0.0
for p in prices:
    priceTotal += p

evens = []
for i in range(0, 21, 2):
    evens.append(i)

countDown = []
i = 100
while i >= 0:
    countDown.append(i)
    i -= 15

names = ["Alice", "Bob", "Amy", "Charlie", "Anna", "David"]
filteredNames = []
for name in names:
    if name.startswith("A"):
        continue
    filteredNames.append(name)

numbers = [10, 20, 30, 60, 40]
foundNumber = None
for n in numbers:
    if n > 50:
        foundNumber = n
        break

multiplicationTable = []
for i in range(1, 11):
    multiplicationTable.append(7 * i)

attempts = 0
lockMessage = None
while attempts < 3:
    attempts += 1
if attempts >= 3:
    lockMessage = "Locked out!"

mixedItems = [1, None, 2, None, 3]
realItems = []
for item in mixedItems:
    if item is None:
        continue
    realItems.append(item)

eCount = 0
for ch in "intermediate":
    if ch == "e":
        eCount += 1
