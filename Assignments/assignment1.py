# Assignment: The Cupcake Counter
# Scenario: A small bakery needs a system to track their flour supply. 
# They need to know if they have enough ingredients to bake cupcakes before they start.

# Final Grade: 90/100
# Reason:
# Code formatting and using global variable within a function, which may lead to errors within the program.
# Overall, good work! You have shown a good understanding of the consept presented to you :)

# Tasks:
# 1. Create a variable 'bakeryName' for the shop's name (String).
# 2. Create a variable 'totalFlour' to track how many kilograms are left (Float).
# 3. Create a function 'checkStock' to see if there is enough flour for an order.
#    - It should take 'flourRequired' as a parameter.
#    - It should return True if there is enough flour, and False if not (Boolean).
# 4. Create a function 'bakeOrder' that handles the baking process.
#    - It should take 'itemName' (String) and 'flourUsed' (Float) as parameters.
#    - It should subtract 'flourUsed' from 'totalFlour'.
#    - It should print a message saying "Baking [itemName]..."

# --- Hints ---
# Hint for checkStock: Use a comparison symbol like >= to compare your stock with what is required.
# Hint for bakeOrder: Since 'totalFlour' is outside the function, you will need to use 'global totalFlour' inside the function to change it.

# --- START YOUR CODE BELOW ---
# (Gaby's submission)
bakeryName = "Sweet Treats Bakery"
TotalFlour = 10.5 
def checkStock(flour):
    return TotalFlour >= flour 
def bakeOrder(itemName, flourUsed):
    global TotalFlour
    TotalFlour -= flourUsed
    print("Bakery " + itemName + "...")
