# Introduction to Python

# 1. What is a variable?
# A variable is basically a container. It's a way for your computer to remember information.
# Think of it like a labeled box. Inside the box is the data, and the label is the name.

# 2. Why use a variable?
# We use them so we don't have to repeat ourselves. 
# If you have a price of 19.99 used in 50 places, using a variable means you only change it once.
# It also makes code look like human language instead of just random numbers.

# 3. How to make a variable:
# Just write the name, an equals sign (=), and the value.
# ('x' is just a variable name to illustrate)
x = 100
userMessage = "Welcome to Python"

# 4. Math in Python
# Python handles math easily with these symbols:
# + for adding
# - for subtracting
# * for multiplying (the asterisk)
# / for dividing (the forward slash)

mathResult = (10 + 5) * 2 # should be 30
print(mathResult)

# 5. Functions in Python
# A function is a reusable block of code. You define it once and "call" it whenever you need it.
# It's like a mini-program inside your program.

def myFirstFunction():
    print("This code is inside a function!")

# Functions can take "inputs" (parameters) and "output" results (return).
def calculateTax(price, taxRate):
    total = price * taxRate
    return total

# Using the function:
finalPrice = calculateTax(100, 0.08)
print(finalPrice)
