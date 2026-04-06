# Python Error Handling

# 1. What is Error Handling?
# Every program can run into problems. A user types the wrong thing,
# a file doesn't exist, or a number gets divided by zero.
# Without error handling, your whole program crashes the moment something goes wrong.
# Think of it like a car's airbag. You hope you never need it,
# but it's there to protect you when things go sideways.

# 2. Try / Except
# The "try" block is where you put the code that might cause a problem.
# The "except" block is where you handle it if it does.
# It's like trying to open a jar. You try to open it,
# and if you can't, you grab a towel for a better grip instead of just giving up.

try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except:
    print("Something went wrong!")

# 3. Catching Specific Errors
# You can (and should) be specific about what kind of error you're catching.
# This way you know exactly what went wrong and can respond to it properly.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Here is another common one — a TypeError happens when you mix incompatible types.
try:
    result = "hello" + 5  # Can't add a string and an int
except TypeError:
    print("Those two types don't work together!")

# 4. The "else" and "finally" blocks
# "else" runs only if no error happened in the try block.
# "finally" always runs, no matter what. Error or not.
# Think of "finally" like locking the front door when you leave the house.
# It doesn't matter how the night went, you always lock the door on the way out.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print("It worked! Result is: " + str(result))
finally:
    print("This always runs.")

# 5. Raising Your Own Errors
# Sometimes you want to throw your own error on purpose.
# Like a bouncer at a club. If someone doesn't meet the rules, you stop them at the door.

def checkAge(age):
    if age < 18:
        raise ValueError("You must be 18 or older.")
    return "Access granted."

try:
    print(checkAge(15))
except ValueError as e:
    print("Error: " + str(e))

# Summary:
# - Try: The code you want to test.
# - Except: What to do if something breaks.
# - Else: Runs only if no error happened.
# - Finally: Always runs, no matter what.
# - Raise: Lets you throw your own custom error.
