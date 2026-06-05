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

from datetime import datetime, date
from typing import List, Dict, Union


orders = [
    {"customer": "Alice",   "item": "croissant",  "orderDate": "2026-05-20", "deliveryDate": "2026-06-01", "status": "delivered"},
    {"customer": "Bob",     "item": "muffin",     "orderDate": "2026-05-25", "deliveryDate": "2026-06-10", "status": "shipped"},
    {"customer": "Charlie", "item": "bagel",      "orderDate": "2026-05-28", "deliveryDate": "2026-06-15", "status": "pending"},
    {"customer": "Diana",   "item": "cookie",     "orderDate": "2026-06-01", "deliveryDate": "2026-06-03", "status": "delivered"},
    {"customer": "Eve",     "item": "scone",      "orderDate": "2026-06-02", "deliveryDate": "2026-06-20", "status": "pending"},
    {"customer": "Frank",   "item": "brownie",    "orderDate": "2026-05-15", "deliveryDate": "2026-05-25", "status": "delivered"},
    {"customer": "Grace",   "item": "croissant",  "orderDate": "2026-06-01", "deliveryDate": "2026-06-05", "status": "shipped"},
    {"customer": "Henry",   "item": "coffee",     "orderDate": "2026-06-03", "deliveryDate": "2026-06-04", "status": "pending"},
]


def daysUntilDelivery(order: Dict[str, str]) -> Union[int, str]:
    """Calculate days between today and the delivery date.

    Args:
        order: An order dict with a 'deliveryDate' key.

    Returns:
        A positive int if future, negative if past, 0 if today,
        or an error message string if the date is malformed.
    """
    try:
        delivery = datetime.strptime(order["deliveryDate"], "%Y-%m-%d").date()
        delta = (delivery - date.today()).days
        return delta
    except (ValueError, KeyError):
        return "Invalid date"


def filterByStatus(orders: List[Dict[str, str]], status: str) -> List[Dict[str, str]]:
    """Return orders that match the given status.

    Args:
        orders: The list of order dicts.
        status: The status to filter by.

    Returns:
        A new list containing only orders with that status.
    """
    return [o for o in orders if o["status"] == status]


def overdueOrders(orders: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Return orders that are not delivered and past their delivery date.

    Args:
        orders: The list of order dicts.

    Returns:
        A list of overdue order dicts.
    """
    today = date.today()
    overdue = []
    for o in orders:
        if o["status"] == "delivered":
            continue
        try:
            delivery = datetime.strptime(o["deliveryDate"], "%Y-%m-%d").date()
            if delivery < today:
                overdue.append(o)
        except ValueError:
            continue
    return overdue


def scheduleSummary(orders: List[Dict[str, str]]) -> Dict[str, int]:
    """Return counts of orders by status and overdue count.

    Args:
        orders: The list of order dicts.

    Returns:
        A dict with total, pending, shipped, delivered, and overdue counts.
    """
    total = len(orders)
    pending = sum(1 for o in orders if o["status"] == "pending")
    shipped = sum(1 for o in orders if o["status"] == "shipped")
    delivered = sum(1 for o in orders if o["status"] == "delivered")
    overdue = len(overdueOrders(orders))
    return {
        "total": total,
        "pending": pending,
        "shipped": shipped,
        "delivered": delivered,
        "overdue": overdue,
    }


def formatDeliveryDate(order: Dict[str, str]) -> str:
    """Return a human-readable string for the delivery date.

    Args:
        order: An order dict with 'customer' and 'deliveryDate' keys.

    Returns:
        A formatted string like "Order for Alice: due Thursday, June 10, 2026".
    """
    try:
        delivery = datetime.strptime(order["deliveryDate"], "%Y-%m-%d")
        formatted = delivery.strftime("%A, %B %d, %Y")
        return f"Order for {order['customer']}: due {formatted}"
    except (ValueError, KeyError):
        return f"Order for {order.get('customer', 'unknown')}: due date unknown"
