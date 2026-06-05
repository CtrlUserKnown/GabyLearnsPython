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


def calculateTotal(basePrice: float, quantity: int, discount: float = 0.0, taxRate: float = 0.08) -> float:
    """Calculate the total price after discount and tax.

    Args:
        basePrice: The base price of one item.
        quantity: How many items.
        discount: Discount as a decimal (0.1 = 10%). Defaults to 0.0.
        taxRate: Tax rate as a decimal. Defaults to 0.08.

    Returns:
        The total rounded to 2 decimal places.
    """
    subtotal = basePrice * quantity
    afterDiscount = subtotal * (1 - discount)
    total = afterDiscount * (1 + taxRate)
    return round(total, 2)


def bulkPricing(basePrice: float, quantity: int) -> float:
    """Apply tiered bulk discounts and return the total.

    Args:
        basePrice: The base price of one item.
        quantity: How many items.

    Returns:
        The total after the bulk discount and tax.
    """
    if quantity >= 21:
        discount = 0.15
    elif quantity >= 11:
        discount = 0.10
    elif quantity >= 6:
        discount = 0.05
    else:
        discount = 0.0
    return calculateTotal(basePrice, quantity, discount)


def applyCoupons(*args: float) -> float:
    """Combine multiple coupon discounts into a single effective discount.

    Args:
        *args: Coupon discount values as decimals (e.g. 0.10, 0.05).

    Returns:
        The combined discount, or 0.0 if no coupons provided.
    """
    if not args:
        return 0.0
    combined = 1.0
    for coupon in args:
        combined *= (1 - coupon)
    return 1 - combined


def makePriceChecker(minPrice: float, maxPrice: float):
    """Return a function that checks if a price falls within a range.

    Args:
        minPrice: The minimum price (inclusive).
        maxPrice: The maximum price (inclusive).

    Returns:
        A lambda that takes a price and returns True if it's in range.
    """
    return lambda price: minPrice <= price <= maxPrice


def formatReceipt(*items) -> None:
    """Print a neatly formatted receipt with itemized totals.

    Args:
        *items: Tuples of (name, price, quantity).
    """
    grandTotal = 0.0
    for name, price, qty in items:
        lineTotal = price * qty
        grandTotal += lineTotal
        print(f"{name:<15} x {qty:<2} = ${lineTotal:>6.2f}")
    print(f"{'':27}--------")
    print(f"{'TOTAL':<21} ${grandTotal:>6.2f}")


# Demonstration
print("=== calculateTotal ===")
print(f"5 croissants at $3.50: ${calculateTotal(3.50, 5)}")
print(f"5 croissants at $3.50 (10% off): ${calculateTotal(3.50, 5, 0.10)}")

print("\n=== bulkPricing ===")
print(f"3 items at $2.00: ${bulkPricing(2.00, 3)}")
print(f"8 items at $2.00: ${bulkPricing(2.00, 8)}")
print(f"15 items at $2.00: ${bulkPricing(2.00, 15)}")
print(f"25 items at $2.00: ${bulkPricing(2.00, 25)}")

print("\n=== applyCoupons ===")
print(f"100.0 with no coupons: {1 - (1 - 0)} = {applyCoupons()}")
print(f"100.0 with 10% off: {applyCoupons(0.10)}")
print(f"100.0 with 10% and 5% off: {applyCoupons(0.10, 0.05)}")

print("\n=== makePriceChecker ===")
checker = makePriceChecker(1.00, 5.00)
print(f"Is $3.00 in range? {checker(3.00)}")
print(f"Is $6.00 in range? {checker(6.00)}")

print("\n=== formatReceipt ===")
formatReceipt(("Croissant", 3.50, 3), ("Muffin", 2.00, 2), ("Coffee", 2.00, 1))
