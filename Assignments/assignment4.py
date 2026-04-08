# Assignment 4: The Bakery's Busy Day
# Due date: 04/26/2026 @ 10:59pm CST

# Scenario: The bakery is having its busiest day yet!
# They have a list of orders to process and need to track how much flour is being used.

# Tasks:
# 1. Create a global variable 'totalFlourUsed' set to 0.
# 2. Create a list called 'orders' with at least 4 items.
#    - Each item in the list should be a dictionary with 'itemName' and 'flourNeeded'.
#    - Example: {"itemName": "Croissant", "flourNeeded": 0.3}
# 3. Create a function 'processOrders' that loops through 'orders'.
#    - For each order, print "Processing: [itemName]"
#    - Add the 'flourNeeded' to 'totalFlourUsed' on each iteration.
# 4. Call 'processOrders', then print the final value of 'totalFlourUsed'.

# --- Hints ---
# Hint for Task 3: Use the 'global' keyword inside 'processOrders' to modify 'totalFlourUsed'.
# Hint for Task 3: Use a for loop to go through each order in the list.
# Hint for Task 3: To access a value inside a dictionary, use order["itemName"].

# --- Grading ---
# 1. totalFlourUsed is a global variable set to 0.                         ( /10 )
# 2. orders list contains at least 4 dictionaries with the correct keys.  ( /20 )
# 3. processOrders loops through all orders and prints each item name.     ( /25 )
# 4. totalFlourUsed is correctly updated on each iteration.                ( /20 )
# 5. Final totalFlourUsed is printed after calling processOrders.          ( /10 )
# 6. Proper Python formatting:                                              ( /15 )
#    - Variables and functions use camelCase.
#    - Code inside functions is consistently indented.
#    - No unnecessary or leftover code.
#                                                                Total:    ( /100 )

# --- START YOUR CODE BELOW ---
