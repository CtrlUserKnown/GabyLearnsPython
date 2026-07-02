# CHALLENGE 10: THE BAKERY'S DATA DASHBOARD (FINAL BOSS!)
# Due date: TBD

# THE SCENARIO: This is the final challenge! The bakery wants an all-in-one
# dashboard that can load sales data, analyze it, and print a beautiful
# report! This assignment combines everything The Gaby has learned from day 1
# to day 20!

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

# "THE FINAL BOSS! CAN THE GABY BECOME THE ULTIMATE CHAMPION?!" — Caine
# --- START YOUR CODE BELOW ---
