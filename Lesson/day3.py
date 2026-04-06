# Python Classes & Inheritance

# 1. What is a Class?
# A class is basically a "blueprint" or a "template" for creating things. 
# It's like a recipe for a cake. The recipe itself isn't a cake, 
# but you use it to bake as many real cakes as you want!

# 2. Why use a Class?
# In programming, we use classes to group together data (variables) 
# and actions (functions) into one object.
# It's a great way to stay organized as our code gets bigger and more complex.

# 3. How to write a Class:
# Use the 'class' keyword and then the name of the class (usually capitalized).
# Inside, we use a special function called __init__ to set up our "template."

class Dog:
    # This runs every time we create a new dog!
    # "self" refers to the specific dog we are creating right now.
    def __init__(self, dogName, dogBreed):
        self.dogName = dogName   # This saves the name to the dog
        self.dogBreed = dogBreed # This saves the breed to the dog

    # A function inside a class is called a "method"
    def barkAtStranger(self):
        print(self.dogName + " says Woof! Who are you?")

# Now we can create real "objects" from our Dog blueprint:
myDog = Dog("Buddy", "Golden Retriever")
myDog.barkAtStranger() # Output: Buddy says Woof! Who are you?

# 4. What is Inheritance?
# Inheritance lets a new class "borrow" everything from an existing class.
# It works just like a child inheriting traits from a parent. 

# If we want a specific type of dog, like a PoliceDog, 
# we don't want to rewrite all the 'dogName' and 'bark' code. 
# We just "inherit" from the Dog class!

class PoliceDog(Dog): # We put the "parent" class in parentheses
    def sniffForClues(self):
        print(self.dogName + " is looking for clues!")

# Now PoliceDog has everything a Dog has, plus its own special skill!
k9 = PoliceDog("Max", "German Shepherd")
k9.barkAtStranger() # Max says Woof! (Inherited from Dog)
k9.sniffForClues()   # Max is looking for clues! (New skill)

# Summary:
# - Class: The Blueprint (Dog)
# - Object: The real thing made from the blueprint (myDog)
# - Inheritance: Getting features from a "Parent" class (PoliceDog inheriting from Dog)