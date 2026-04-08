# Python Classes & Inheritance

# 1. What is a Class?
# A class is basically a "blueprint" or a "template" for creating things. 
# It's like a recipe for a cake. The recipe itself isn't a cake, 
# but you use it to bake as many real cakes as you want!

# 2. Why use a Class?
# In programming, we use classes to group together data (variables) 
# and actions (functions) into one object.
# Think of it like a player profile in a video game. One profile holds
# your name, your level, your health, and your abilities all in one place.
# A class does the same thing for your code.

# 3. How to write a Class:
# Use the 'class' keyword and then the name of the class (usually capitalized).
# Inside, we use a special function called __init__ to set up our "template."
# Think of __init__ like the assembly line at a car factory. Every time a new
# car rolls off the line, it gets stamped with a color, a model, and a serial number.
# __init__ does that stamping for every new object you create.

class Dog:
    # This runs every time we create a new dog!
    # "self" refers to the specific dog we are creating right now.
    def __init__(self, dogName, dogBreed):
        self.dogName = dogName
        self.dogBreed = dogBreed

    # A function inside a class is called a "method"
    def barkAtStranger(self):
        print(self.dogName + " says Woof! Who are you?")

# Now we can create real "objects" from our Dog blueprint:
myDog = Dog("Buddy", "Golden Retriever")
myDog.barkAtStranger() # Output: Buddy says Woof! Who are you?

# 4. What is Inheritance?
# Inheritance lets a new class "borrow" everything from an existing class.
# It works just like a child inheriting traits from a parent.
# You don't have to teach a child to walk from scratch if they already
# picked it up naturally. They just add their own skills on top.

# If we want a specific type of dog, like a PoliceDog,
# we don't want to rewrite all the 'dogName' and 'bark' code.
# We just "inherit" from the Dog class!

class PoliceDog(Dog): # We put the "parent" class in parentheses
    def sniffForClues(self):
        print(self.dogName + " is looking for clues!")

# Now PoliceDog has everything a Dog has, plus its own special skill!
k9 = PoliceDog("Max", "German Shepherd")
k9.barkAtStranger() # Max says Woof! (Inherited from Dog)
k9.sniffForClues()  # Max is looking for clues! (New skill)

# Summary:
# - Class: The Blueprint (Dog)
# - Object: The real thing made from the blueprint (myDog)
# - Inheritance: Getting features from a "Parent" class (PoliceDog inheriting from Dog)