# Assignment 3: The Bakery Gets Bigger
# Due date: 05/17/2026 @ 10:59pm CST
# Lessons: day1 - day5

# Scenario: The bakery is growing! Instead of just tracking flour,
# they now want a proper system to manage their baked goods.

# Tasks:
# 1. Create a class called 'BakedGood'.
#    - It should store 'itemName' and 'flourRequired' when a new item is created.
#    - Add a method called 'describe' that prints something like:
#      "Croissant requires 0.3kg of flour."

# 2. Create a class called 'PremiumBakedGood' that inherits from 'BakedGood'.
#    - Add a new attribute called 'extraIngredient' (something special about this item).
#    - Add a method called 'describeSpecial' that prints something like:
#      "Our special Croissant is made with: imported butter."

# 3. Create at least two regular BakedGood objects and one PremiumBakedGood object.
#    - Call 'describe' on each of them.
#    - Call 'describeSpecial' on your PremiumBakedGood.

# --- Hints ---
# Hint for Task 1: Your __init__ should take 'itemName' and 'flourRequired' as parameters.
# Hint for Task 2: Put the parent class in parentheses: class PremiumBakedGood(BakedGood).
# Hint for Task 2: PremiumBakedGood's __init__ should also accept 'extraIngredient' as a parameter.

# --- Grading ---
# 1. BakedGood class exists and stores itemName and flourRequired.        ( /15 )
# 2. describe method prints the correct output.                            ( /15 )
# 3. PremiumBakedGood inherits from BakedGood.                            ( /20 )
# 4. PremiumBakedGood stores extraIngredient and describeSpecial works.   ( /20 )
# 5. At least two BakedGood objects and one PremiumBakedGood are created. ( /15 )
# 6. Add comments explaining your code. in plain english.                  ( /10 )
# 7. Proper Python formatting:                                             ( /5 )
#    - Classes use PascalCase (BakedGood, PremiumBakedGood).
#    - Attributes and methods use camelCase (itemName, describeSpecial).
#    - Code inside classes and methods is consistently indented.
#    - No unnecessary or leftover code.
#                                                                Total:    ( /100 )

# --- START YOUR CODE BELOW ---

