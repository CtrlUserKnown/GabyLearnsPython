# Assignment 8: The Bakery's Delivery Schedule
# Due date: TBD

# Scenario: The bakery now delivers! They need a system to track delivery
# dates, schedules, and find out when things are running late or early.

# Tasks:
# 1. Create a list called 'orders'. Each order should be a dictionary with:
#    - 'customer' (string): customer name
#    - 'item' (string): what they ordered
#    - 'orderDate' (string): when the order was placed ("YYYY-MM-DD")
#    - 'deliveryDate' (string): when it's due ("YYYY-MM-DD")
#    - 'status' (string): "pending", "shipped", or "delivered"
#    Include at least 6 orders with a mix of statuses and dates.

# 2. Create a function 'daysUntilDelivery' that takes an order dict.
#    - Calculate the number of days between today and the delivery date.
#    - Return a positive int if the delivery is in the future.
#    - Return a negative int if it's overdue.
#    - Return 0 if it's due today.
#    - Handle errors if the date string is malformed.

# 3. Create a function 'filterByStatus' that takes the orders list and
#    a status string, and returns a new list of orders with that status.

# 4. Create a function 'overdueOrders' that takes the orders list.
#    - Return a list of orders where status is NOT "delivered" AND
#      the delivery date is before today.

# 5. Create a function 'scheduleSummary' that takes the orders list.
#    - Return a dict with:
#      - 'total': total number of orders
#      - 'pending': count of pending orders
#      - 'shipped': count of shipped orders
#      - 'delivered': count of delivered orders
#      - 'overdue': count of overdue orders

# 6. Create a function 'formatDeliveryDate' that takes an order dict.
#    - Return a string like: "Order for Alice: due Thursday, June 10, 2026"
#    - Use strftime to format the date nicely.

# 7. Add docstrings to ALL functions.

# --- Hints ---
# Hint for Task 2: from datetime import datetime, date
# Hint for Task 2: delivery = datetime.strptime(order["deliveryDate"], "%Y-%m-%d").date()
# Hint for Task 6: deliveryDate = datetime.strptime(...) then use .strftime("%A, %B %d, %Y")

# --- Grading ---
# 1. orders list has 6+ orders with correct structure.             ( /10 )
# 2. daysUntilDelivery calculates correctly (future/past/today).    ( /15 )
# 3. filterByStatus returns correct filtered list.                  ( /10 )
# 4. overdueOrders identifies overdue non-delivered orders.         ( /15 )
# 5. scheduleSummary returns correct counts.                        ( /10 )
# 6. formatDeliveryDate returns a nicely formatted string.          ( /10 )
# 7. All functions have docstrings.                                 ( /10 )
# 8. Python best practices & formatting:                            ( /20 )
#    - Functions have type hints.
#    - Descriptive variable names.
#    - Consistent indentation (4 spaces).
#    - Error handling for date parsing.
#    - No unnecessary or commented-out code.
#                                                        Total:    ( /100 )

# --- START YOUR CODE BELOW ---
