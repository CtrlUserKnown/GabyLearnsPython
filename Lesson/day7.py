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

# 5. Mutability
# Objects created from a class are mutable. That means you can change their
# attributes after they've been created.
# Think of it like a whiteboard. Once something is written on it, you can
# erase it and write something new. The whiteboard is still the same one,
# just with updated information on it.

myDog.dogName = "Max"  # We just changed Buddy's name to Max
print(myDog.dogName)   # Output: Max

# This is different from something like a String, which is immutable.
# Once a String is created, Python won't let you change individual parts of it.
# Think of a String like text carved into stone. You can't go back and
# chisel out one letter. You'd have to carve a whole new stone.

myString = "Buddy"
# myString[0] = "R"  # This would cause a TypeError — you can't do this

# With a class object, you can update individual attributes freely.
# Each object also keeps its own copy of the data, independent of other objects.
# Changing one dog's name does not affect any other dog.

dogOne = Dog("Buddy", "Golden Retriever")
dogTwo = Dog("Rex", "Labrador")

dogOne.dogName = "Charlie"
print(dogOne.dogName)  # Output: Charlie
print(dogTwo.dogName)  # Output: Rex (completely unaffected)

# Summary:
# - Class: The Blueprint (Dog)
# - Object: The real thing made from the blueprint (myDog)
# - Inheritance: Getting features from a "Parent" class (PoliceDog inheriting from Dog)
# - Mutability: Objects can be changed after creation. Each object owns its own data.
