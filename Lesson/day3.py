# Python Operators & Conditionals

# 1. What are Operators?
# Operators are symbols that let you do things with your data.
# Think of them like tools in a toolbox. Each one has a specific job.

# Math Operators (you already know these from day1):
# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# %  Modulo (gives you the remainder after dividing)
# ** Exponent (raises a number to a power)

print(10 % 3)  # Output: 1 (10 divided by 3 leaves a remainder of 1)
print(2 ** 4)  # Output: 16 (2 to the power of 4)

# 2. Comparison Operators
# These compare two values and always return True or False.
# Think of them like a scale. You put something on each side and it tips one way or the other.

# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

print(10 == 10)  # True
print(10 != 5)   # True
print(7 > 10)    # False

# 3. Logical Operators
# These let you combine multiple comparisons together.
# Think of them like the words "and", "or", and "not" in a sentence.

# and - Both sides must be True
# or  - At least one side must be True
# not - Flips True to False, and False to True

hasTicket = True
isOldEnough = True

print(hasTicket and isOldEnough)  # True (both are True)
print(hasTicket or isOldEnough)   # True (at least one is True)
print(not hasTicket)              # False (flips True to False)

# 4. What are Conditionals?
# Conditionals let your program make decisions.
# Think of it like a fork in the road. Depending on the condition,
# your code takes one path or the other.

# The "if" statement runs a block of code only if the condition is True.

temperature = 85

if temperature > 80:
    print("It's hot outside!")

# 5. if / else
# You can add an "else" block to handle the case when the condition is False.
# If the first road is blocked, take the other one.

temperature = 60

if temperature > 80:
    print("It's hot outside!")
else:
    print("The weather is nice.")

# 6. if / elif / else
# "elif" stands for "else if." It lets you check multiple conditions in order.
# Python checks each one from top to bottom and stops at the first True one.

score = 72

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 7. Putting it all together
# You can use operators inside your conditionals to build more specific checks.

age = 20
hasID = True

if age >= 18 and hasID:
    print("You're good to go!")
else:
    print("Sorry, you can't enter.")

# Summary:
# - Math Operators: +, -, *, /, %, **
# - Comparison Operators: ==, !=, >, <, >=, <=  (always return True or False)
# - Logical Operators: and, or, not  (combine comparisons)
# - if: Runs code when a condition is True.
# - elif: Checks another condition if the first was False.
# - else: Runs when none of the above conditions were True.
