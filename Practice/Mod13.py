"""
Text Formatting and Analysis Module

String manipulation, formatting, pattern matching,
and text processing utilities.
"""

itemName = "croissant"
quantity = 12
price = 3.5

formattedSale = f"Sold {quantity} {itemName}s for ${quantity * price:.2f}"

joined = " - ".join(["a", "b", "c"])

fruits = "apple,banana,grape"
splitFruits = fruits.split(",")

cleaned = "  hello world  ".strip()

replaced = "the cat sat".replace("cat", "dog")

findIndex = "hello world".find("world")

alpha = "hello123".isalpha()
digit = "hello123".isdigit()
alnum = "hello123".isalnum()

fraction = 1/3
asPercent = f"{fraction:.1%}"

bigNumber = 1234567
withCommas = f"{bigNumber:,}"

import re

text = "the baker bakes beautiful bagels"
bWords = re.findall(r"\bb\w+", text)
