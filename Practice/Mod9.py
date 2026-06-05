"""
System Configuration and Import Utilities

Provides system-wide configuration, utility functions,
and import demonstrations for the application framework.
"""

import math

appName = "GabyLearnsPython"
appVersion = "1.0"

sqrtResult = math.sqrt(144)

circumference = 2 * math.pi * 5

from math import ceil, floor
roundedUp = ceil(4.3)
roundedDown = floor(4.9)


def getAppInfo():
    return f"{appName} v{appVersion}"


def divideAndRound(a, b):
    result = a / b
    return math.ceil(result)


currentModule = __name__

if __name__ == "__main__":
    print(f"{appName} v{appVersion} is ready!")
