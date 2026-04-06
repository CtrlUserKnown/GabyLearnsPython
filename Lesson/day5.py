# Python Loops

# 1. What is a Loop?
# A loop is a way to repeat a block of code more than once without rewriting it.
# Think of it like a playlist on repeat. Instead of hitting play 10 times manually,
# you just set it to loop and it handles the rest.

# 2. Why use a Loop?
# If you need to do the same thing multiple times (check every item in a list,
# count down from 10, keep asking a user for input), loops save you from
# copy-pasting the same lines over and over.

# 3. The For Loop
# A "for" loop runs through a collection of things one at a time.
# Think of it like going through a grocery list. You look at each item,
# one by one, until you reach the end of the list.

fruits = ["apples", "bananas", "oranges"]

for fruit in fruits:
    print("I need to buy: " + fruit)

# You can also loop through a range of numbers using range().
# range(5) gives you the numbers 0, 1, 2, 3, 4

for i in range(5):
    print("Rep number: " + str(i))

# 4. The While Loop
# A "while" loop keeps running as long as a condition is True.
# It's like a vending machine. It keeps waiting for you to make a selection.
# As long as you haven't picked anything, it just sits there and waits.

countdown = 5

while countdown > 0:
    print("Counting down: " + str(countdown))
    countdown = countdown - 1

print("Done!")

# Be careful with while loops! If your condition never becomes False,
# it will run forever. That's called an "infinite loop" and it will crash your program.

# 5. Break and Continue
# Sometimes you need to jump out of a loop early, or skip a step.

# "break" stops the loop completely, like hitting the emergency stop button.
for number in range(10):
    if number == 5:
        break
    print(number)

# "continue" skips the current step and moves to the next one.
# Like skipping a song you don't like on the playlist.
for number in range(10):
    if number == 5:
        continue
    print(number)

# Note: Python does not have a built-in "do-while" loop like some other languages.
# But you can mimic the same behavior using awhile loop with a break.
# A do-while runs the code block first, THEN checks the condition.

# Here is how you fake a do-while in Python:
while True:
    print("This runs at least once!")
    break  # We break immediately, but in a real case you'd check a condition here.

# Summary:
# - For Loop: Use when you know how many times you want to repeat something.
# - While Loop: Use when you want to keep going until something changes.
# - Break: Stops the loop early.
# - Continue: Skips the current step and keeps going.
