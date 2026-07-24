# Changing Case in a String by 'Methods' :
name = " Astra Quark X "
print(name.title())   #>>> Rahul Sharma 
print(name.upper())   #>>> RAHUL SHARMA 
print(name.lower())   #>>> rahul sharma

# Escape Sequence :
print("Hello \nWorld")     # New Line
print("Hello \tWorld")     # Insert Tab Space (4 Spaces)
print("Hello \\ World")    # \\ inserts \ : Hello \ World
print("\'Hello World\'")   # \' inserts ' : 'Hello World'
print("\"Hello World\"")   # \" inserts " : "Hello World"
print("Hello\bWorld")      # Backspace - Deletes 'o'
print("Hello hello\rWorld")      #>>> World hello
  # Cursor goes to the start of the line. The text after it, 'World', overwrites the original text and replaces 'Hello'.
  # \r moves the cursor to the beginning of the current line without going to a new line.
  # Any text printed after \r overwrites the existing text on that line.

# Stripping Whitespace from Strings :
print(name.rstrip())       # Removes the whitespace from right end temporarily 
print(name.lstrip())       # Removes the whitespace from left end temporarily 
print(name.strip())        # Removes the whitespace from both ends temporarily 

# Printing Variables :
  # Basic Print :
    a = "World!"
    print("Hello ",a)
  # Formatted Strings (F-Strings) :
    a = "World"
    b = 1
    print(f"Hello {a} {b}")
  # .format() Method :
    a = "Hello"
    b = "World"
    c = "Astra"
    d = "Quark X"
    print("{} {} , {name1} {name2}!".format(a,b,name1 = c,name2 = d))
  # % Formatting :
    name = "AstraQuarkX"
    year = 2026
    version = 1.0
    print("Hello, %s \nYear = %d %i \nVersion = %.1f" % (name,year,year,version))

