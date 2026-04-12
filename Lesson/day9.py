# Python File I/O (Input and Output)

# File I/O is how your program reads from and writes to files on your computer.
# Think of it like a notebook. You can open it, read what's inside,
# write something new, or add to what's already there.

# 1. Opening a File
# You use the open() function. It takes two things: the file name and the "mode."
# The mode tells Python what you want to do with the file.

# Common modes:
# "r" - Read. Opens the file to read it. (The file must already exist.)
# "w" - Write. Creates a new file, or WIPES an existing one and starts fresh.
# "a" - Append. Adds to the end of an existing file without deleting anything.
# "x" - Create. Makes a new file, but fails if it already exists.


# 2. Writing to a File
# "w" mode will create the file if it doesn't exist.
# If it does exist, it will overwrite everything inside.

file = open("bakery_log.txt", "w")
file.write("Croissant - sold 12\n")   # \n moves to the next line
file.write("Muffin - sold 8\n")
file.close()  # Always close the file when you're done!


# 3. Reading a File
# "r" mode lets you read what's inside.

file = open("bakery_log.txt", "r")
contents = file.read()   # Reads the entire file as one string
print(contents)
file.close()


# 4. The "with" Statement (The Better Way)
# Manually calling close() every time is easy to forget.
# The "with" statement handles it for you automatically.
# Think of it like a self-closing door. You walk through it, do your thing,
# and it closes behind you on its own.

with open("bakery_log.txt", "r") as file:
    contents = file.read()
    print(contents)
# File is already closed here, no need to call file.close()


# 5. Reading Line by Line
# Instead of reading everything at once, you can go through it one line at a time.

with open("bakery_log.txt", "r") as file:
    for line in file:
        print("Item: " + line.strip())  # strip() removes the \n at the end


# 6. Appending to a File
# "a" mode adds to the end without touching what's already there.

with open("bakery_log.txt", "a") as file:
    file.write("Bagel - sold 5\n")


# 7. Combining with Error Handling
# If the file doesn't exist and you try to read it, Python will crash.
# Wrapping it in a try/except protects your program.

try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file doesn't exist!")


# Summary:
# - open(file, mode): Opens a file. Modes are "r", "w", "a", and "x".
# - file.read(): Reads the whole file.
# - file.write(): Writes a string to the file.
# - with open(...) as file: The preferred way. Closes the file automatically.
# - FileNotFoundError: The error to catch when a file doesn't exist.
