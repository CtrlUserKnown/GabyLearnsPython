# Assignment 2: The Bakery's Price Check
# Due date: 04/12/2026 @ 10:59pm CST

# Scenario: The bakery needs a simple system to check orders before they go out.
# They want to make sure orders are priced correctly and flag anything unusual.

# Tasks:
# 1. Create a variable 'itemPrice' (Float) and 'quantity' (Int) for an order.
# 2. Calculate the 'orderTotal' by multiplying them together.
# 3. Create a variable 'discount' (Float, between 0 and 1) to apply to large orders.
#    - Apply it to 'orderTotal' only if the quantity is 10 or more.
# 4. Create a function 'checkOrder' that takes 'orderTotal' as a parameter.
#    - If the total is over 100, print "Large order! Flagging for review."
#    - If the total is between 50 and 100 (inclusive), print "Standard order."
#    - If the total is under 50, print "Small order."
# 5. Call 'checkOrder' with your calculated total.

# --- Hints ---
# Hint for Task 3: Use an if statement with >= to check the quantity before applying the discount.
# Hint for Task 4: Use if / elif / else and comparison operators to check the ranges.
# Hint for Task 4: To check if a number is between two values, you can use 'and' to combine two comparisons.

# --- Grading ---
# 1. itemPrice, quantity, and orderTotal are created correctly.              ( 15/15 )
# 2. Discount is applied only when quantity >= 10.                          ( 10/20 )
# 3. checkOrder function exists and takes orderTotal as a parameter.        ( 15/15 )
# 4. All three conditions (over 100, 50-100, under 50) are handled.        ( 25/25 )
# 5. checkOrder is called with the correct value.                           ( 10/10 )
# 6. Proper Python formatting:                                              ( 15/15 )
#    - Variables and functions use camelCase.
#    - Code inside functions is consistently indented.
#    - No unnecessary or leftover code.
#                                                               Total:      ( 84/100 )

# --- START YOUR CODE BELOW ---

itemPrice = 5.50 # +5
quantity = 12 # +5
orderTotal = itemPrice * quantity   # +5
discount = 0.10 # +5
if quantity >= 10: # (1) -10 | +5 (kinda correct, look at note)
    orderTotal = orderTotal * (1- discount) # (ps.1) -1

def checkOrder (orderTotal): # +15 | (ps.2) -1
    if orderTotal > 100: # +10
        print ("Large order! Flagging for review.") # (ps) -1
    elif 50 <= orderTotal <= 100:
        print ("Standard order.") # (ps.2) -1
    else: 
        print ("Small order.") # (ps.2) -1

checkOrder (orderTotal) # (ps.2) -1

# Notes:
# (1) the if statement that checks the quantity should be in the function. Since its outside of the functions scope, nothing actually happens.
# (ps.1) the spacing needs improvements better. line 42: if you dont add the right spacing while doing calculations, the code may not do what you intend it to do.
# (ps.2) line 44, 46, 48, 50, 52: when writing or calling functions, the function name and the paranthesies should not be seperate from one another. i.e "functionName(parameter)" not "functionName_(parameter)"
# Overall: Pay attention to the little details. The order in which things are done makes a differences in the code, especially with math. use comments to think out the code before actually writing it.
