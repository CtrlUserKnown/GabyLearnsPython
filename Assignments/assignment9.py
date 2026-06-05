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
