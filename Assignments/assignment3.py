# Assignment 3: The Bakery's Busy Day

# Scenario: The bakery is having its busiest day yet! They need a system
# to process a list of orders and keep a running total of flour used.

# Tasks:
# 1. Create a global variable called 'totalFlourUsed' and set it to 0.

# 2. Create a list called 'orders' with at least 4 items.
#    Each item should be a list with two values: [itemName, flourRequired].
#    Example: ["Croissant", 0.3]

# 3. Create a function called 'processOrders' that loops through the orders list.
#    - For each order, print something like: "Baking Croissant... used 0.3kg of flour."
#    - It should add each order's flourRequired to totalFlourUsed.
#    - Use the 'global' keyword to modify totalFlourUsed inside the function.

# 4. Create a function called 'findLargeOrders' that loops through the orders list.
#    - If an order requires more than 0.5kg of flour, print:
#      "Large order alert: Wedding Cake needs 2.0kg of flour."
#    - If no large orders exist, print: "No large orders today."

# 5. Call both functions and then print the final totalFlourUsed.

# --- Hints ---
# Hint for Task 3: Use a for loop to go through each order. orders[0] would be
#   the first order, and inside that, orders[0][0] is the name, orders[0][1] is the flour.
# Hint for Task 3: Don't forget 'global totalFlourUsed' at the top of the function.
# Hint for Task 4: Use an if statement inside your for loop to check flourRequired.

# --- Grading ---
# 1. Global variable totalFlourUsed is declared and starts at 0.              ( /10 )
# 2. orders list has at least 4 items, each with a name and flourRequired.    ( /15 )
# 3. processOrders loops through orders and prints the correct output.        ( /25 )
# 4. processOrders correctly updates totalFlourUsed using the global keyword. ( /25 )
# 5. findLargeOrders correctly identifies and prints large orders.            ( /25 )
#                                                                   Total:    ( /100 )

# --- START YOUR CODE BELOW ---
