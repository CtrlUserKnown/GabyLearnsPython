# Python Common Methods

# Methods are built-in functions that belong to a specific data type.
# You call them directly on the value using a dot: value.method()

# 1. String Methods
# Strings come with a lot of useful tools for working with text.

name = "  gaby learns python  "

print(name.strip())       # Removes whitespace from both ends: "gaby learns python"
print(name.upper())       # All caps: "  GABY LEARNS PYTHON  "
print(name.lower())       # All lowercase (already lowercase here)
print(name.title())       # Capitalizes each word: "  Gaby Learns Python  "

sentence = "Python is fun and Python is easy"
print(sentence.replace("Python", "Coding"))  # Swaps out words
print(sentence.count("Python"))              # How many times "Python" appears: 2
print(sentence.startswith("Python"))         # True
print(sentence.endswith("easy"))             # True
print(sentence.split(" "))                   # Breaks the sentence into a list by spaces


# 2. List Methods
# Lists have methods for adding, removing, and organizing items.

fruits = ["banana", "apple", "cherry"]

fruits.append("mango")       # Adds to the end
fruits.remove("apple")       # Removes a specific item
fruits.sort()                # Sorts alphabetically
fruits.reverse()             # Flips the order
print(fruits.index("mango")) # Finds the position of an item
print(len(fruits))           # len() is a built-in that gives you the count


# 3. Dictionary Methods
# Dictionaries store key-value pairs. These methods help you navigate them.

person = {"name": "Gaby", "age": 20, "city": "Chicago"}

print(person.keys())         # All the keys: name, age, city
print(person.values())       # All the values: Gaby, 20, Chicago
print(person.items())        # Both, as pairs: ("name", "Gaby"), etc.
print(person.get("age"))     # Safe way to get a value (won't crash if key is missing)

person.update({"age": 21})   # Updates an existing key
person.pop("city")           # Removes a key-value pair


# 4. Type Conversion Methods
# Sometimes you need to switch between types.

numAsString = "42"
print(int(numAsString))      # String -> Int: 42
print(float(numAsString))    # String -> Float: 42.0

num = 99
print(str(num))              # Int -> String: "99"

myList = [1, 2, 2, 3, 3, 3]
print(set(myList))           # Removes duplicates: {1, 2, 3}


# Summary:
# - String methods: strip, upper, lower, replace, split, count, startswith, endswith
# - List methods: append, remove, sort, reverse, index
# - Dictionary methods: keys, values, items, get, update, pop
# - Type conversion: int(), float(), str(), set()
