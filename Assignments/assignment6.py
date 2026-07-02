# BONUS ROUND 6: THE BAKERY'S MENU BOARD!
# Due date: TBD

# THE CHALLENGE: The bakery wants to redesign their menu board! They have lists
# of items, prices, and categories. They need you to transform this data
# into something more useful using comprehensions!

# Tasks:
# 1. Create three lists:
#    - 'itemNames': at least 8 bakery items (strings).
#    - 'prices': matching prices (floats, in dollars).
#    - 'categories': matching categories (strings like "pastry", "bread", "drink").

# 2. Use a list comprehension to create 'formattedMenu'.
#    - Each element should be a string like: "Croissant ($3.50)"
#    - The item name should be title-cased.
#    - The price should show 2 decimal places.

# 3. Use a dict comprehension to create 'priceByItem'.
#    - Keys are item names (title-cased), values are prices.

# 4. Use a dict comprehension to create 'itemsByCategory'.
#    - Keys are categories, values are LISTS of item names in that category.
#    - Hint: Use a set to get unique categories, then filter items for each.

# 5. Use a list comprehension to create 'affordableItems'.
#    - Items with a price under $3.00.
#    - Each element should be a tuple like (itemName, price).

# 6. Use a list comprehension to create 'discountedPrices'.
#    - Apply a 15% discount to all prices.
#    - Round each to 2 decimal places.

# 7. Use a set comprehension to create 'uniqueCategories'.
#    - A set of all unique categories.

# 8. Add a comment above each comprehension explaining in plain English
#    what it does and why. Write it as if explaining to a non-programmer.

# --- Hints ---
# Hint for Task 4: Use a loop or comprehension: for cat in set(categories):
# Hint for Task 4: Inside the loop: [item for i, item in enumerate(itemNames) if categories[i] == cat]
# Hint for Task 6: Discounted price = round(price * 0.85, 2)

# --- Grading ---
# 1. Three source lists exist with 8+ items.                      ( /10 )
# 2. formattedMenu uses a list comprehension correctly.           ( /10 )
# 3. priceByItem uses a dict comprehension correctly.             ( /10 )
# 4. itemsByCategory uses a dict comprehension correctly.         ( /15 )
# 5. affordableItems uses a list comprehension with filtering.    ( /10 )
# 6. discountedPrices uses a list comprehension correctly.        ( /10 )
# 7. uniqueCategories uses a set comprehension correctly.         ( /10 )
# 8. Comments explain each comprehension in plain English.        ( /10 )
# 9. Python best practices & formatting:                           ( /15 )
#    - Descriptive variable names (no single-letter names).
#    - Consistent indentation (4 spaces).
#    - No unnecessary or commented-out code.
#    - Comprehensions are readable (not overly complex).
#                                                        Total:    ( /100 )

# "COMPREHENSIONS? COMPREHENSIBLE!" — Caine
# --- START YOUR CODE BELOW ---
