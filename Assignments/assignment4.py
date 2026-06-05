# Assignment 4: The Bakery's Restock
# Due date: 05/24/2026 @ 10:59pm CST

# Scenario: A shipment just arrived at the bakery! The delivery includes several
# ingredients, but not all of them are usable. Some items are expired and need
# to be rejected. The bakery needs a system to sort through the shipment,
# accept good items, and update their stock accordingly.

# Tasks:
# 1. Create a global dictionary 'pantry' that stores at least 4 ingredients
#    and their current stock amount (in kg). Example: {"flour": 5.0, "sugar": 3.0}

# 2. Create a list called 'shipment'. Each item in the list should be a dictionary
#    with three keys: 'ingredient', 'amount', and 'expired'.
#    - Include at least 6 items. Some should be expired (True), some not (False).
#    - Some ingredients should match what's already in the pantry. Some can be new.

# 3. Create a function 'processItem' that takes one shipment item as a parameter.
#    - If the item is expired, print a rejection message and do nothing else.
#    - If the item is not expired, add its amount to the pantry.
#      - If the ingredient is already in the pantry, add to the existing amount.
#      - If it's a new ingredient, add it as a new entry in the pantry.

# 4. Loop through the shipment list and call 'processItem' on each one.

# 5. After the loop, print the final state of the pantry.

# 6. Add a comment above each block of code explaining what it does in plain English.
#    Write it as if you're explaining it to someone who has never seen code before.

# --- Hints ---
# Hint for Task 3: Use the 'global' keyword to access and modify the pantry.
# Hint for Task 3: To check if a key exists in a dictionary, use: if key in dictionary.
# Hint for Task 5: To print the pantry nicely, you can loop through pantry.items().
# Hint for Task 6: A good comment tells you WHY or WHAT, not just repeats the code.
#   Bad:  # sets flour to 5.0
#   Good: # This is the bakery's current stock. Each ingredient tracks how much we have in kg.

# --- Grading ---
# 1. pantry is a global dictionary with at least 4 ingredients.            ( /10 )
# 2. shipment is a list of dictionaries with the correct keys.             ( /10 )
# 3. processItem correctly rejects expired items.                          ( /15 )
# 4. processItem correctly updates existing and adds new ingredients.      ( /15 )
# 5. The shipment is looped through and processItem is called on each.     ( /15 )
# 6. The final pantry is printed after the loop.                           ( /10 )
# 7. Comments are present above each block and written in plain English.   ( /20 )
#    - Comments explain what the code does, not just restate it.
#    - Writing is clear enough that a non-programmer could follow along.
# 8. Proper Python formatting:                                             ( /5  )
#    - Variables and functions use camelCase.
#    - Code inside functions is consistently indented.
#    - No unnecessary or leftover code.
#                                                            Total:        ( /100 )

# --- START YOUR CODE BELOW ---

# This is the bakery's current stock. Each ingredient tracks how much we have in kg.
pantry = {
    "flour": 5.0,
    "sugar": 3.0,
    "butter": 2.0,
    "eggs": 1.5
}

# This is the delivery shipment. Each item has the ingredient name, how much (in kg),
# and whether it has expired. Expired items cannot be accepted.
shipment = [
    {"ingredient": "flour",       "amount": 3.0,  "expired": False},
    {"ingredient": "sugar",       "amount": 2.0,  "expired": True},
    {"ingredient": "butter",      "amount": 1.5,  "expired": False},
    {"ingredient": "vanilla",     "amount": 0.5,  "expired": False},
    {"ingredient": "baking soda", "amount": 1.0,  "expired": True},
    {"ingredient": "eggs",        "amount": 2.0,  "expired": False},
]


# This function looks at one item from the shipment and decides what to do with it.
# If it's expired, we throw it away. If it's good, we add it to the pantry stock.
def processItem(item):
    global pantry
    if item["expired"]:
        # The item has expired, so we cannot accept it. Let the baker know.
        print(f"Rejecting expired {item['ingredient']} ({item['amount']}kg).")
    else:
        # The item is fresh — check if we already have this ingredient in the pantry.
        if item["ingredient"] in pantry:
            # We already have this ingredient, so we add the new amount to what we already have.
            pantry[item["ingredient"]] += item["amount"]
        else:
            # This is a new ingredient we don't have yet, so we add it to the pantry.
            pantry[item["ingredient"]] = item["amount"]
        print(f"Accepted {item['ingredient']} ({item['amount']}kg).")


# Go through each item in the shipment one by one and process it.
for item in shipment:
    processItem(item)

# Print a nice summary of everything we now have in the pantry.
print("\nFinal pantry contents:")
for ingredient, amount in pantry.items():
    print(f"  {ingredient}: {amount}kg")
