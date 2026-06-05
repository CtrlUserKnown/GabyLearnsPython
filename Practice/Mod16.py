"""
Data Import and Export Module

Functions for reading, writing, and transforming
data between CSV and JSON formats.
"""

import csv
import json

csvRows = []
with open('sales.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        csvRows.append(row)

csvDictRows = []
with open('sales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        csvDictRows.append(row)

outputData = [
    ["name", "age", "city"],
    ["Gaby", 25, "Austin"],
    ["Bob", 30, "Dallas"],
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(outputData)

outputDictData = [
    {"name": "Gaby", "age": "25", "city": "Austin"},
    {"name": "Bob", "age": "30", "city": "Dallas"},
]

with open('output_dict.csv', 'w', newline='') as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(outputDictData)

sampleData = {
    "bakery": "Sweet Treats",
    "items": [
        {"name": "croissant", "price": 3.50},
        {"name": "muffin", "price": 2.00},
    ],
    "isOpen": True,
}

with open('data.json', 'w') as f:
    json.dump(sampleData, f, indent=2)

with open('data.json', 'r') as f:
    loadedData = json.load(f)

jsonString = '{"name": "Test", "value": 42}'
parsedJson = json.loads(jsonString)

pythonDict = {"language": "Python", "version": 3.11}
jsonOutput = json.dumps(pythonDict, indent=2)
