# Introduction to Python - Day 1

# 1. What is a variable?
# A variable is basically a container. It's a way for your computer to remember information.
# Think of it like a labeled box. If you have a box labeled "Toys," you know exactly 
# what is inside without having to open it every time. 

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
# It's basically a super-fast calculator that never gets tired.

mathResult = (10 + 5) * 2 # should be 30
print(mathResult)

# 5. Functions in Python
# A function is a reusable block of code. You define it once and "call" it whenever you need it.
# It's a lot like a "Coffee Machine." You press one button (the function name), 
# and it does a bunch of steps for you (grinding beans, boiling water, pouring) 
# without you having to do them manually every time!

def myFirstFunction():
    print("This code is inside a function!")

# Functions can take "inputs" (parameters) and "output" results (return).
# Just like coffee beans and water go in, and hot coffee comes out!
def calculateTax(price, taxRate):
    total = price * taxRate
    return total

# Using the function:
finalPrice = calculateTax(100, 0.08)
print(finalPrice)
