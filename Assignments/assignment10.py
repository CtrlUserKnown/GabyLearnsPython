# Assignment 10: The Bakery's Data Dashboard (Capstone)
# Due date: TBD

# Scenario: This is the final challenge! The bakery wants an all-in-one
# dashboard that can load sales data, analyze it, and print a beautiful
# report. This assignment combines everything you've learned from day 1
# to day 20.

# Tasks:

# 1. Create a function 'loadData' that loads data from a CSV file.
#    - Use csv.DictReader to read the file.
#    - Convert numeric fields.
#    - Skip bad rows gracefully with a warning message.
#    - Return the cleaned data as a list of dicts.
#    - If the file doesn't exist, create sample data with createSampleData().

# 2. Create a function 'createSampleData' that writes a CSV file with
#    at least 20 rows of realistic bakery sales data across 7 days.
#    Include columns: date, item, category, quantity, price.
#    - Items should come from at least 8 different products.
#    - Categories: "pastry", "bread", "drink", "dessert".
#    - Use random module to generate realistic quantities (5-50).

# 3. Create a function 'analyzeData' that takes the sales list and
#    returns a dictionary with ALL of the following:
#    - 'totalRevenue': sum of all revenue
#    - 'totalItemsSold': sum of all quantities
#    - 'totalOrders': number of rows
#    - 'averageOrderValue': totalRevenue / totalOrders
#    - 'bestDay': date with the highest revenue
#    - 'bestSellingItem': item name with highest total quantity
#    - 'categoryBreakdown': dict of category -> totalRevenue
#    - 'dailyRevenue': dict of date -> totalRevenue (sorted by date)
#    - 'itemsSoldPerDay': dict of date -> totalItems (sorted by date)

# 4. Create a function 'printReport' that takes the analysis dict and
#    prints a nicely formatted report to the terminal.
#    Use f-strings with proper alignment and formatting.
#    Example format:
#    ========================================
#       BAKERY SALES DASHBOARD
#    ========================================
#    Report generated: 2026-06-04 14:30:00
#
#    SUMMARY
#      Total Revenue:    $1,234.56
#      Total Items Sold: 456
#      Total Orders:     20
#      Avg Order Value:  $61.73
#      Best Day:         2026-06-02
#      Best Selling:     croissant
#
#    CATEGORY BREAKDOWN
#      pastry   $567.89
#      bread    $345.67
#      ...

# 5. Create a function 'exportReport' that saves the analysis dict
#    as a JSON file called "dashboard_report.json".

# 6. Create a function 'main' (using the if __name__ == "__main__"
#    pattern) that runs the full pipeline:
#    - Load data
#    - Analyze data
#    - Print report to terminal
#    - Export report to JSON

# 7. Add docstrings with type hints to ALL functions.

# --- Hints ---
# Hint for Task 2: Use random.randint(5, 50) for quantities, random.choice() for items.
# Hint for Task 3: For bestDay, group sales by date and sum revenue.
# Hint for Task 4: Use f"{'label:':<20} ${value:>8.2f}" for alignment.
# Hint for Task 6: if __name__ == "__main__": main()

# --- Grading ---
# 1. loadData loads and cleans CSV correctly.                       ( /10 )
# 2. createSampleData generates realistic data.                      ( /10 )
# 3. analyzeData returns ALL required fields.                        ( /20 )
# 4. printReport prints a well-formatted readable report.            ( /15 )
# 5. exportReport saves JSON correctly.                              ( /10 )
# 6. main() ties everything together with if __name__ pattern.       ( /5  )
# 7. All functions have docstrings with type hints.                  ( /10 )
# 8. Python best practices & formatting:                             ( /20 )
#    - Modular design: each function does ONE thing.
#    - Clear, descriptive names throughout.
#    - Consistent indentation (4 spaces).
#    - Comprehensive error handling.
#    - No unnecessary or commented-out code.
#    - Code is clean and production-ready.
#                                                        Total:    ( /100 )

# --- START YOUR CODE BELOW ---

import csv
import json
import random
from datetime import datetime
from typing import List, Dict, Optional


ITEMS = [
    ("croissant", "pastry", 3.50),
    ("muffin", "pastry", 2.00),
    ("bagel", "bread", 1.50),
    ("cookie", "dessert", 1.00),
    ("scone", "pastry", 2.50),
    ("brownie", "dessert", 2.75),
    ("coffee", "drink", 2.00),
    ("tea", "drink", 1.50),
    ("danish", "pastry", 3.00),
    ("loaf", "bread", 4.00),
]

DATES = ["2026-05-25", "2026-05-26", "2026-05-27", "2026-05-28",
         "2026-05-29", "2026-05-30", "2026-05-31"]


def createSampleData(filepath: str = "bakery_dashboard.csv") -> None:
    """Generate a realistic CSV file with at least 20 rows of sales data.

    Args:
        filepath: Path to write the CSV file.
    """
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "item", "category", "quantity", "price"])
        for _ in range(25):
            date = random.choice(DATES)
            item, category, price = random.choice(ITEMS)
            quantity = random.randint(5, 50)
            writer.writerow([date, item, category, quantity, price])


def loadData(filepath: str = "bakery_dashboard.csv") -> List[Dict[str, object]]:
    """Load and clean sales data from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A list of cleaned sale dicts with numeric fields converted.
    """
    try:
        with open(filepath, "r", newline="") as f:
            reader = csv.DictReader(f)
            sales = []
            for row in reader:
                try:
                    row["quantity"] = int(row["quantity"])
                    row["price"] = float(row["price"])
                    row["revenue"] = round(row["quantity"] * row["price"], 2)
                    sales.append(row)
                except (ValueError, KeyError):
                    print(f"Warning: Skipping bad row: {row}")
            return sales
    except FileNotFoundError:
        print(f"File '{filepath}' not found. Creating sample data...")
        createSampleData(filepath)
        return loadData(filepath)


def analyzeData(sales: List[Dict[str, object]]) -> Dict[str, object]:
    """Compute all analytics from the sales data.

    Args:
        sales: The list of cleaned sale dicts.

    Returns:
        A dict with all required analysis fields.
    """
    totalRevenue = sum(s["revenue"] for s in sales)
    totalItemsSold = sum(s["quantity"] for s in sales)
    totalOrders = len(sales)
    averageOrderValue = round(totalRevenue / totalOrders, 2) if totalOrders else 0.0

    dailyRevenue = {}
    itemsSoldPerDay = {}
    for s in sales:
        date = s["date"]
        dailyRevenue[date] = dailyRevenue.get(date, 0) + s["revenue"]
        itemsSoldPerDay[date] = itemsSoldPerDay.get(date, 0) + s["quantity"]
    for d in dailyRevenue:
        dailyRevenue[d] = round(dailyRevenue[d], 2)
    bestDay = max(dailyRevenue, key=dailyRevenue.get)

    itemQuantities = {}
    for s in sales:
        item = s["item"]
        itemQuantities[item] = itemQuantities.get(item, 0) + s["quantity"]
    bestSellingItem = max(itemQuantities, key=itemQuantities.get)

    categoryBreakdown = {}
    for s in sales:
        cat = s["category"]
        categoryBreakdown[cat] = categoryBreakdown.get(cat, 0) + s["revenue"]
    for c in categoryBreakdown:
        categoryBreakdown[c] = round(categoryBreakdown[c], 2)

    sortedDates = sorted(dailyRevenue.keys())
    dailyRevenueSorted = {d: dailyRevenue[d] for d in sortedDates}
    itemsSoldPerDaySorted = {d: itemsSoldPerDay[d] for d in sortedDates}

    return {
        "totalRevenue": round(totalRevenue, 2),
        "totalItemsSold": totalItemsSold,
        "totalOrders": totalOrders,
        "averageOrderValue": averageOrderValue,
        "bestDay": bestDay,
        "bestSellingItem": bestSellingItem,
        "categoryBreakdown": categoryBreakdown,
        "dailyRevenue": dailyRevenueSorted,
        "itemsSoldPerDay": itemsSoldPerDaySorted,
    }


def printReport(analysis: Dict[str, object]) -> None:
    """Print a nicely formatted dashboard report to the terminal.

    Args:
        analysis: The analysis dict from analyzeData.
    """
    print("=" * 44)
    print("         BAKERY SALES DASHBOARD")
    print("=" * 44)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"  Report generated: {now}")
    print()

    print("  SUMMARY")
    print(f"    {'Total Revenue:':<20} ${analysis['totalRevenue']:>8.2f}")
    print(f"    {'Total Items Sold:':<20} {analysis['totalItemsSold']:>8}")
    print(f"    {'Total Orders:':<20} {analysis['totalOrders']:>8}")
    print(f"    {'Avg Order Value:':<20} ${analysis['averageOrderValue']:>8.2f}")
    print(f"    {'Best Day:':<20} {analysis['bestDay']:>8}")
    print(f"    {'Best Selling:':<20} {analysis['bestSellingItem']:>8}")
    print()

    print("  CATEGORY BREAKDOWN")
    for cat, rev in sorted(analysis["categoryBreakdown"].items()):
        print(f"    {cat:<12} ${rev:>8.2f}")
    print()

    print("  DAILY REVENUE")
    for date, rev in analysis["dailyRevenue"].items():
        print(f"    {date}  ${rev:>8.2f}")
    print()

    print("  ITEMS SOLD PER DAY")
    for date, qty in analysis["itemsSoldPerDay"].items():
        print(f"    {date}  {qty:>8}")
    print("=" * 44)


def exportReport(analysis: Dict[str, object], filepath: str = "dashboard_report.json") -> None:
    """Save the analysis dict as a JSON file.

    Args:
        analysis: The analysis dict from analyzeData.
        filepath: Path for the output JSON file.
    """
    with open(filepath, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"Report exported to {filepath}")


def main() -> None:
    """Run the full dashboard pipeline: load, analyze, print, export."""
    sales = loadData()
    analysis = analyzeData(sales)
    printReport(analysis)
    exportReport(analysis)


if __name__ == "__main__":
    main()
