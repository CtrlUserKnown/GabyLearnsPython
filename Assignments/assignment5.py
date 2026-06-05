# Assignment 5: The Bakery's Recipe Module
# Due date: TBD

# Scenario: The bakery wants to organize all their recipes into a module.
# Instead of having recipe code scattered everywhere, they want a single
# file they can import whenever they need to look up or scale a recipe.

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

# --- START YOUR CODE BELOW ---

"""
Recipe management module for the bakery.

Provides functions to look up recipes, scale them to different
yields, list available recipes, and check if the pantry has enough
ingredients for a given recipe.
"""

recipes = {
    "croissant": {"flour": 2.0, "sugar": 0.5, "butter": 1.0, "yield": 12},
    "muffin":    {"flour": 1.5, "sugar": 0.8, "butter": 0.5, "yield": 10},
    "bagel":     {"flour": 3.0, "sugar": 0.2, "butter": 0.3, "yield": 15},
    "cookie":    {"flour": 1.0, "sugar": 0.6, "butter": 0.7, "yield": 24},
}


def getRecipe(itemName):
    """Return the recipe dict for itemName, or None if not found."""
    if itemName in recipes:
        return recipes[itemName]
    return None


def scaleRecipe(itemName, desiredYield):
    """Scale a recipe to a desired yield. Return scaled dict or None if not found."""
    recipe = getRecipe(itemName)
    if recipe is None:
        return None
    ratio = desiredYield / recipe["yield"]
    scaled = {}
    for ingredient, amount in recipe.items():
        if ingredient == "yield":
            continue
        scaled[ingredient] = round(amount * ratio, 2)
    return scaled


def listRecipes():
    """Return a sorted list of all available recipe names."""
    return sorted(recipes.keys())


def hasIngredients(recipeName, pantry):
    """Check if the pantry has enough of each ingredient for the given recipe."""
    recipe = getRecipe(recipeName)
    if recipe is None:
        return False
    for ingredient, amount in recipe.items():
        if ingredient == "yield":
            continue
        if pantry.get(ingredient, 0) < amount:
            return False
    return True
