"""
Game State Management Module

Manages global game state including player stats,
scoring, inventory, and game control functions.
"""

appName = "My Game"


def localTest():
    x = 10
    return x


lives = 3


def loseLife():
    global lives
    lives -= 1


playerName = "Player One"


def changeName():
    global playerName
    playerName = "New Player"


totalSales = 0


def makeSale(amount):
    global totalSales
    totalSales += amount


color = "blue"


def localColor():
    color = "red"
    return color


counter = 0


def incrementCounter():
    global counter
    counter += 1


def getDiscount():
    discountRate = 0.15
    return discountRate


isGameOver = False


def endGame():
    global isGameOver
    isGameOver = True


def outerFunction():
    message = "Hello from outer"

    def innerFunction():
        return message

    return innerFunction()


budget = 500


def spendMoney(cost):
    global budget
    budget -= cost
