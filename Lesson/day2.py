# Python Data Types - Part 2
# (This file is the next step after learning the basics in app.py)

# Python uses different data types to know what kind of information you are working with.
# Think of these as different types of "boxes" for your data.

# 1. Strings - for text like words, sentences, or even just one letter.
# You always put these inside "quotes" or 'quotes'.
# These are like labels on a folder—words that tell you what something is.
# x = "Hello World"

# 2. Ints (Integers) - for whole numbers that don't have decimals.
# Good for counting things.
# These are like "Whole Apples." You can't have 1.5 whole apples, only 1, 2, or 3.
# x = 20

# 3. Floats (Floating Point) - for numbers that DO have decimals.
# Useful for measurements or prices.
# These are more like "Measuring Cups." You can have 1.5 cups or 0.75 cups.
# x = 20.5 

# 4. Booleans - for things that are only True or False.
# Like a light switch: it is either on or off.
# is_it_raining = True

# 5. Lists - for when you want to store a bunch of things in one place.
# You use [square brackets] and commas to separate them.
# It's like a grocery bag where you put many items (milk, bread, eggs) in one place.
# shopping_list = ["apples", "milk", "eggs"]


# Function Structure Overview
# Functions are like "recipes". You define them once, and then you can use them whenever you want.
# Here is how they are built:

# def - This tells Python you are starting a function.
# functionName - This is the name you give it (try to make it descriptive).
# (parameters) - These are the things the function needs to do its job (the ingredients).
# : - The colon starts the "body" of the function.
# Indentation - Everything inside the function MUST be tabbed/spaced over.
# return - This is how the function "gives back" the result of its work.

# Example:
# def addNumbers(num1, num2):
#     result = num1 + num2
#     return result


def illustrateDataTypes(userName, age, currentPoints):
    # 1. String - greeting the user
    welcome = "Hello " + userName
    print(welcome)

    # 2. Int - doing some simple math with whole numbers
    yearsUntilOneHundred = 100 - age
    
    # 3. Float - using decimals for a bonus multiplier
    bonusMultiplier = 1.5
    totalScore = currentPoints * bonusMultiplier
    print("Your total score is: " + str(totalScore))

    # 4. Boolean - checking a condition (True or False)
    isHighScore = totalScore > 100
    print("Is this a high score? " + str(isHighScore))

    # 5. List - gathering all our info into one place
    summary = [userName, age, totalScore, isHighScore]
    return summary

# To use it:
# print(illustrateDataTypes("Alice", 25, 80))

# make a function
# the function should get the radius of a circle
# the formula is Radius = Circumference / (2 x π)
# the Circumference is 20
# return that value

