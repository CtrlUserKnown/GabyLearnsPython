"""
Mathematical Computation Module

Utility functions and constants for mathematical
operations, statistics, and random generation.
"""

import math
import random
import statistics

ceilResult = math.ceil(3.2)
floorResult = math.floor(3.8)

sqrtResult = math.sqrt(144)
powResult = math.pow(2, 10)

circleArea = math.pi * 3 ** 2

randomInt = random.randint(1, 100)

randomColor = random.choice(["red", "blue", "green", "yellow"])

sample = random.sample([10, 20, 30, 40, 50], 2)

data = [10, 20, 30, 40, 50]
meanValue = statistics.mean(data)
medianValue = statistics.median(data)

rounded = round(3.14159, 2)

nums = [4, 7, 2, 9, 5]
minNum = min(nums)
maxNum = max(nums)
sumNums = sum(nums)

factorialResult = math.factorial(5)

gcdResult = math.gcd(12, 8)
