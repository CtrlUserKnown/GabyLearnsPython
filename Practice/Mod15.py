"""
Date and Time Management Module

Utilities for date parsing, formatting, scheduling,
and time-based calculations.
"""

from datetime import datetime, date, timedelta

now = datetime.now()

currentYear = now.year
currentMonth = now.month
currentDay = now.day

christmas = date(2026, 12, 25)

formattedDate = now.strftime("%B %d, %Y")

parsedDate = datetime.strptime("2026-12-25", "%Y-%m-%d")

daysUntilChristmas = (christmas - date.today()).days

oneWeekLater = date.today() + timedelta(days=7)

thirtyDaysAgo = date.today() - timedelta(days=30)

todayFormatted = date.today().strftime("%A, %B %d, %Y")

isChristmasFuture = christmas > date.today()

from datetime import time
specificTime = time(14, 30)

date1 = date(2026, 1, 1)
date2 = date(2026, 12, 31)
daysBetween = (date2 - date1).days
