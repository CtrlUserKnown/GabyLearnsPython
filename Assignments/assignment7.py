# Assignment 7: The Bakery's Price Calculator
# Due date: TBD

# Scenario: The bakery needs a flexible pricing system. Different customers
# get different discounts, and some orders have special rules. They need
# you to build a system using advanced functions.

# Tasks:
# 1. Create a function 'calculateTotal' that takes:
#    - 'basePrice' (float) - the base price of an item.
#    - 'quantity' (int) - how many items.
#    - 'discount' (float, optional, default=0.0) - discount as decimal (0.1 = 10%).
#    - 'taxRate' (float, optional, default=0.08) - tax rate as decimal.
#    Calculate: subtotal = basePrice * quantity
#               afterDiscount = subtotal * (1 - discount)
#               total = afterDiscount * (1 + taxRate)
#    Return the total rounded to 2 decimal places.

# 2. Create a function 'bulkPricing' that takes:
#    - 'basePrice' (float)
#    - 'quantity' (int)
#    Apply these discounts based on quantity:
#      - 1-5:    no discount
#      - 6-10:   5% discount (0.05)
#      - 11-20:  10% discount (0.10)
#      - 21+:    15% discount (0.15)
#    Call calculateTotal with the appropriate discount and return the result.

# 3. Create a function 'applyCoupons' that takes:
#    - *args: any number of coupon discount values (floats, e.g. 0.10, 0.05)
#    - Return the COMBINED discount. If no coupons, return 0.0.
#    - Hint: Combined discount means you can't just add them.
#      Use: 1 - (1 - c1) * (1 - c2) * ...

# 4. Create a function 'makePriceChecker' that takes a 'minPrice' and 'maxPrice'.
#    - It should RETURN a new function (a lambda) that takes a price and
#      returns True if the price is between minPrice and maxPrice (inclusive).
#    - This is a "closure" - a function that remembers the values from
#      when it was created.

# 5. Create a function 'formatReceipt' that takes *items as tuples of
#    (name, price, quantity) and prints a formatted receipt.
#    - Each line should show: "Croissant x 3  = $10.50"
#    - Items should be aligned neatly (use f-string formatting with widths).
#    - At the bottom, print the total.

# 6. Add docstrings to ALL functions.

# --- Hints ---
# Hint for Task 3: combined = 1 - (1 - d1) * (1 - d2)  for two discounts.
# Hint for Task 4: def makePriceChecker(minP, maxP): return lambda p: minP <= p <= maxP
# Hint for Task 5: Use f"{name:<15} x {qty:<2} = ${total:>6.2f}" for alignment.

# --- Grading ---
# 1. calculateTotal works with all parameters (including defaults).  ( /15 )
# 2. bulkPricing applies correct discount tiers.                    ( /15 )
# 3. applyCoupons combines multiple discounts correctly.             ( /10 )
# 4. makePriceChecker returns a working closure/lambda.              ( /10 )
# 5. formatReceipt prints a correctly formatted receipt.             ( /10 )
# 6. All functions have docstrings.                                  ( /10 )
# 7. Code is called/tested at the bottom (demonstrate it works).     ( /10 )
# 8. Python best practices & formatting:                             ( /20 )
#    - Functions have type hints (e.g., def calc(x: float) -> float).
#    - Docstrings follow a consistent format (Args / Returns).
#    - Descriptive variable names, consistent indentation.
#    - No unnecessary or commented-out code.
#                                                        Total:    ( /100 )

# --- START YOUR CODE BELOW ---
