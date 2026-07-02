# CHALLENGE 5: THE BAKERY'S RECIPE MODULE!
# Due date: TBD

# THE SCENARIO: The bakery wants to organize all their recipes into a module!
# Instead of having recipe code scattered everywhere, they want a single
# file they can import whenever they need to look up or scale a recipe!

# Tasks:
# 1. Create a dictionary called 'recipes' that stores at least 4 recipes.
#    - Each recipe should have: 'flour' (float, kg), 'sugar' (float, kg),
#      'butter' (float, kg), and 'yield' (int, number of items).
#    - Example: "croissant": {"flour": 2.0, "sugar": 0.5, "butter": 1.0, "yield": 12}
#    - Include at least: croissant, muffin, bagel, and cookie.

# 2. Create a function 'getRecipe' that takes an item name as a parameter.
#    - If the item exists in recipes, return the recipe dict.
#    - If it doesn't exist, return None.

# 3. Create a function 'scaleRecipe' that takes an item name and a
#    desired yield as parameters.
#    - Look up the recipe using getRecipe.
#    - If the recipe doesn't exist, return None.
#    - Calculate the scaling ratio: desiredYield / recipeYield.
#    - Return a new dict with each ingredient amount scaled.
#    - Round each amount to 2 decimal places.

# 4. Create a function 'listRecipes' that returns a sorted list of
#    all available recipe names.

# 5. Create a function 'hasIngredients' that takes a recipe name and
#    a pantry dict (ingredient -> available kg).
#    - Look up the recipe. Return False if it doesn't exist.
#    - Check if the pantry has enough of EACH ingredient.
#    - Return True if all ingredients are available, False otherwise.

# 6. Add a comment block at the top of the file (after the header)
#    explaining what this module does, like a real module docstring.

# --- Hints ---
# Hint for Task 3: ratio = desiredYield / recipes[itemName]["yield"]
# Hint for Task 3: Use a dict comprehension or a loop to scale each ingredient.
# Hint for Task 5: Iterate over the recipe's ingredients and check if
#                  pantry.get(ingredient, 0) >= amount.

# --- Grading ---
# 1. recipes dict exists with at least 4 correct entries.           ( /10 )
# 2. getRecipe returns the recipe dict or None correctly.           ( /10 )
# 3. scaleRecipe correctly scales all ingredients.                  ( /15 )
# 4. scaleRecipe returns None for unknown items.                    ( /5  )
# 5. listRecipes returns a sorted list of recipe names.             ( /10 )
# 6. hasIngredients correctly checks pantry against a recipe.       ( /15 )
# 7. Module docstring at the top explains the module's purpose.      ( /10 )
# 8. Python best practices & formatting:                            ( /15 )
#    - Functions have docstrings explaining what they do.
#    - Variables and functions use clear, descriptive names.
#    - Consistent indentation (4 spaces).
#    - No unnecessary or commented-out code.
#    - Use snake_case for variables and functions.
# 9. Proper error handling:                                         ( /10 )
#    - scaleRecipe handles missing items gracefully.
#    - hasIngredients handles missing pantry keys safely.
#                                                        Total:    ( /100 )

# "MODULE POWER, ACTIVATED!" — Caine
# --- START YOUR CODE BELOW ---
