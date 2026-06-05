"""
Text and Data Transformation Utilities

Utility functions for string manipulation, list operations,
dictionary management, and data type conversions.
"""

paddedString = "  hello world  "
strippedString = paddedString.strip()

lowerTitle = "hello world"
titledString = lowerTitle.title()

original = "I like cats"
replaced = original.replace("cats", "dogs")

sentence = "The quick brown fox"
wordList = sentence.split()

unsortedNums = [5, 2, 8, 1, 9]
sortedNums = sorted(unsortedNums)

editList = ["a", "b", "c", "d", "e"]
editList.remove("c")
editList.append("f")

personDict = {"name": "Gaby", "age": 25, "city": "Austin"}
dictKeys = list(personDict.keys())
dictValues = list(personDict.values())

missingValue = personDict.get("nickname", None)

updatedDict = personDict.copy()
updatedDict.update({"nickname": "Gabs"})
updatedDict.pop("age")

numString = "77"
doubledNum = int(numString) * 2

dupList = [1, 2, 2, 3, 3, 3]
uniqueList = list(set(dupList))

wordBank = ["apple", "banana", "carrot", "avocado", "cherry", "grape"]
aCount = 0
for word in wordBank:
    if "a" in word:
        aCount += 1
