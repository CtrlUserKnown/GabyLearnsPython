"""
Data Transformation Service

Module for transforming, filtering, and processing
collections of data using functional patterns.
"""

numbers = list(range(1, 11))

squares = [n ** 2 for n in numbers]

evens = [n for n in numbers if n % 2 == 0]

words = ["apple", "banana", "avocado", "blueberry", "cherry"]

wordLengths = [len(w) for w in words]

aWords = [w for w in words if w.startswith("a")]

wordLengthDict = {w: len(w) for w in words}

firstLetters = {w[0] for w in words}

items = ["croissant", "muffin", "bagel", "cookie"]
numberedItems = [f"{i}: {item}" for i, item in enumerate(items)]
