"""
Function Utility Library

Demonstrates advanced Python function features including
*args, **kwargs, lambda functions, closures, and map/filter patterns.
"""


def sumAll(*args):
    return sum(args)


def buildProfile(**kwargs):
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())


def applyDiscount(discount):
    return lambda price: price * (1 - discount)


double = lambda x: x * 2

stringNums = ["1", "2", "3"]
parsedNums = list(map(lambda x: int(x), stringNums))

mixedNums = [3, 15, 7, 22, 1, 18]
bigNums = list(filter(lambda x: x > 10, mixedNums))

pairs = [("a", 3), ("b", 1), ("c", 2)]
sortedPairs = sorted(pairs, key=lambda x: x[1])

total = sumAll(1, 2, 3, 4, 5)

profile = buildProfile(name="Gaby", age=25, city="Austin")
