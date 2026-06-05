"""
Inventory and Collection Manager

Manages grouped data structures, frequency counting,
and set-based operations for data processing.
"""

from collections import defaultdict, Counter

salesItems = ["croissant", "muffin", "croissant", "bagel",
              "croissant", "muffin", "cookie", "bagel", "croissant"]

salesCount = defaultdict(int)
for item in salesItems:
    salesCount[item] += 1

croissantCount = salesCount["croissant"]

wordList = ["apple", "banana", "avocado", "blueberry", "apricot", "cherry"]
groupedByLetter = defaultdict(list)
for word in wordList:
    groupedByLetter[word[0]].append(word)

frequency = Counter(salesItems)

topTwo = frequency.most_common(2)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

unionResult = setA | setB
intersectionResult = setA & setB
diffResult = setA - setB

isSubset = setA.issubset(setB)
