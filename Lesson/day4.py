# Python Scopes - Local, Global, and Beyond

# 1. What is Scope?
# Scope is like a "boundary" or a "zone" where a variable can be seen and used. 
# You can think of it like being in a car. 

# 2. Local Scope (Inside the Car)
# When you create a variable inside a function, it is "local" to that function.
# It's your own phone inside the car. Only the people in the car (the code 
# inside the function) can see it or use it. Once you step out of the car 
# (the function finishes), that phone is gone!

def myCar():
    myPhone = "iPhone 15" # This is a local variable
    print("Inside the car, I have my: " + myPhone)

myCar()
# print(myPhone) # This would cause an ERROR because myPhone only exists inside myCar.

# 3. Global Scope (The Weather Outside)
# A global variable is created outside of any functions. It is available to 
# EVERYONE in the script. 
# It's the weather outside. Whether you are inside your car, inside a 
# house, or just walking, you can see if it's "Sunny" or "Raining."

weather = "Sunny" # This is a global variable

def checkWeather():
    print("From inside the function, I see it is: " + weather)

checkWeather()
print("Outside the function, I see it is: " + weather)

# 4. The "L.E.G.B." Rule
# When you ask Python for a variable, it looks for it in a specific order, 
# much like a set of Matryoshka dolls (Russian nesting dolls):

# L - Local: First, it looks inside the current function (the smallest doll).
# E - Enclosing: Then, it looks in any "parent" functions (if functions are nested).
# G - Global: Next, it looks at the top level of your script (the big doll).
# B - Built-in: Finally, it looks at Python's own internal tools (like 'print' or 'len').

# 5. The "Global" Keyword (Reaching Out of the Car)
# Usually, you can see a global variable from inside a function, but you 
# can't CHANGE it. It's like looking through the car window—you can see 
# the rain, but you can't reach out and stop it. 

# If you REALLY want to change a global variable from inside a function, 
# you have to use the 'global' keyword.

score = 0 # Global

def increaseScore():
    global score # This tells Python "I want to talk to the global 'score' variable!"
    score = score + 10

increaseScore()
print("Total score is now: " + str(score)) # Output: 10

# 6. Shadowing (Two variables with the same name)
# You can have a local variable and a global variable with the same name. 
# Python will always pick the "closest" one (the Local one).
# This is called "Shadowing."

name = "Global Name" # The big doll

def sayName():
    name = "Local Name" # The small doll (Shadows the global one)
    print("Inside the function: " + name)

sayName()
print("Outside the function: " + name)

# Summary:
# - Local: Variables inside a function.
# - Global: Variables outside all functions.
# - L.E.G.B.: The order Python follows to find your variables.
# - Global Keyword: Used to modify a global variable from inside a function.
