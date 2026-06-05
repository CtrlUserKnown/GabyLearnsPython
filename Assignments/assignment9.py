# Assignment 9: The Bakery's Sales Report
# Due date: TBD

# Scenario: The bakery needs a system to read their daily sales from a CSV
# file, process the data, and export a summary report as JSON. They also
# need to be able to combine data from multiple days.

# Tasks:

# 1. Create a function 'createSampleCSV' that writes a sample CSV file
#    called "bakery_sales.csv" with the following columns:
#    date,item,quantity,price
#    Include at least 10 rows of data across at least 3 different dates.
#    Call this function at the start so the data exists for testing.

# 2. Create a function 'loadSales' that takes a filepath.
#    - Read the CSV file using csv.DictReader.
#    - Convert 'quantity' to int and 'price' to float for each row.
#    - Calculate and add a 'revenue' field (quantity * price) to each row.
#    - Return a list of cleaned order dicts.
#    - Use error handling: skip rows that can't be parsed, print a warning.

# 3. Create a function 'dailySummary' that takes the sales list.
#    - Group sales by date.
#    - For each date, calculate: totalRevenue, totalItems, orderCount.
#    - Return a dict like: {"2026-06-04": {"totalRevenue": 100.0, ...}, ...}

# 4. Create a function 'topSellers' that takes the sales list and an
#    optional 'limit' parameter (default=3).
#    - Find the top N items by total quantity sold across all dates.
#    - Return a list of tuples: [(itemName, totalQuantity), ...] sorted
#      from most sold to least.

# 5. Create a function 'exportReport' that takes the sales list and
#    a filepath.
#    - Call dailySummary and topSellers.
#    - Combine everything into one report dict:
#      {
#          "generated": "2026-06-04 14:30:00",  (use datetime.now())
#          "totalRevenue": <sum of all revenue>,
#          "totalItemsSold": <sum of all quantities>,
#          "dailySummaries": <from dailySummary>,
#          "topSellers": <from topSellers>,
#      }
#    - Write the report as JSON to the given filepath.
#    - Return the report dict.

# 6. Create a function 'runReport' that ties it all together.
#    - Takes 'inputFile' and 'outputFile' as parameters.
#    - Calls loadSales then exportReport.
#    - Handles errors gracefully (file not found, etc.).
#    - Prints progress messages as it runs.

# 7. Add docstrings with type hints to ALL functions.

# --- Hints ---
# Hint for Task 3: Collect unique dates, then filter sales for each date.
# Hint for Task 4: Use a dict to sum quantities per item, then sort.
# Hint for Task 6: try/except FileNotFoundError around loadSales.

# --- Grading ---
# 1. createSampleCSV creates valid CSV data.                       ( /10 )
# 2. loadSales reads and cleans data correctly.                    ( /15 )
# 3. dailySummary groups by date and calculates correctly.         ( /15 )
# 4. topSellers returns correctly sorted top items.                ( /10 )
# 5. exportReport creates a complete report dict.                  /15 )
# 6. runReport ties everything together with error handling.       ( /10 )
# 7. All functions have docstrings with type hints.                ( /10 )
# 8. Python best practices & formatting:                           ( /15 )
#    - Each function does ONE thing (modular design).
#    - Descriptive function and variable names.
#    - Consistent indentation (4 spaces).
#    - Error handling where appropriate.
#    - No unnecessary or commented-out code.
#                                                        Total:    ( /100 )

# --- START YOUR CODE BELOW ---

import csv
import json
from datetime import datetime
from typing import List, Dict, Tuple, Optional


def createSampleCSV() -> None:
    """Write a sample CSV file called bakery_sales.csv with at least 10 rows."""
    with open("bakery_sales.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "item", "quantity", "price"])
        writer.writerow(["2026-06-01", "croissant", 12, 3.50])
        writer.writerow(["2026-06-01", "muffin", 8, 2.00])
        writer.writerow(["2026-06-01", "coffee", 15, 2.00])
        writer.writerow(["2026-06-02", "bagel", 10, 1.50])
        writer.writerow(["2026-06-02", "croissant", 20, 3.50])
        writer.writerow(["2026-06-02", "cookie", 25, 1.00])
        writer.writerow(["2026-06-03", "scone", 6, 2.50])
        writer.writerow(["2026-06-03", "muffin", 14, 2.00])
        writer.writerow(["2026-06-03", "brownie", 9, 2.75])
        writer.writerow(["2026-06-03", "coffee", 18, 2.00])


def loadSales(filepath: str) -> List[Dict[str, object]]:
    """Read a CSV sales file and return a list of cleaned order dicts.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A list of dicts with quantity (int), price (float), and revenue (float).
    """
    sales = []
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["quantity"] = int(row["quantity"])
                row["price"] = float(row["price"])
                row["revenue"] = round(row["quantity"] * row["price"], 2)
                sales.append(row)
            except (ValueError, KeyError):
                print(f"Warning: Skipping bad row: {row}")
    return sales


def dailySummary(sales: List[Dict[str, object]]) -> Dict[str, Dict[str, float]]:
    """Group sales by date and calculate totals for each day.

    Args:
        sales: The list of cleaned sales dicts.

    Returns:
        A dict mapping dates to their summary stats.
    """
    summary = {}
    for s in sales:
        date = s["date"]
        if date not in summary:
            summary[date] = {"totalRevenue": 0.0, "totalItems": 0, "orderCount": 0}
        summary[date]["totalRevenue"] += s["revenue"]
        summary[date]["totalItems"] += s["quantity"]
        summary[date]["orderCount"] += 1
    for d in summary:
        summary[d]["totalRevenue"] = round(summary[d]["totalRevenue"], 2)
    return summary


def topSellers(sales: List[Dict[str, object]], limit: int = 3) -> List[Tuple[str, int]]:
    """Return the top N best-selling items by total quantity.

    Args:
        sales: The list of cleaned sales dicts.
        limit: How many top sellers to return (default 3).

    Returns:
        A list of (itemName, totalQuantity) tuples sorted descending.
    """
    totals = {}
    for s in sales:
        item = s["item"]
        totals[item] = totals.get(item, 0) + s["quantity"]
    sorted_items = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:limit]


def exportReport(sales: List[Dict[str, object]], filepath: str) -> Dict[str, object]:
    """Generate a full report and write it as JSON.

    Args:
        sales: The list of cleaned sales dicts.
        filepath: Where to write the JSON report.

    Returns:
        The report dict.
    """
    daily = dailySummary(sales)
    top = topSellers(sales)
    totalRevenue = round(sum(s["revenue"] for s in sales), 2)
    totalItemsSold = sum(s["quantity"] for s in sales)

    report = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "totalRevenue": totalRevenue,
        "totalItemsSold": totalItemsSold,
        "dailySummaries": daily,
        "topSellers": top,
    }

    with open(filepath, "w") as f:
        json.dump(report, f, indent=2)

    return report


def runReport(inputFile: str, outputFile: str) -> None:
    """Load sales from CSV, generate a report, and save as JSON.

    Args:
        inputFile: Path to the input CSV file.
        outputFile: Path for the output JSON report.
    """
    print(f"Loading sales from {inputFile}...")
    try:
        sales = loadSales(inputFile)
    except FileNotFoundError:
        print(f"Error: File '{inputFile}' not found.")
        return

    print(f"Loaded {len(sales)} sales entries. Generating report...")
    report = exportReport(sales, outputFile)
    print(f"Report saved to {outputFile}")
    print(f"Total Revenue: ${report['totalRevenue']}")
    print(f"Total Items Sold: {report['totalItemsSold']}")


createSampleCSV()
runReport("bakery_sales.csv", "bakery_report.json")
