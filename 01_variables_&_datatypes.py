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
# DOUBT print("Hello\rWorld")
print("Hello\bWorld")      # Backspace - Deletes 'o'

# Stripping Whitespace from Strings :
print(name.rstrip())       # Removes the whitespace from right end temporarily 
print(name.lstrip())       # Removes the whitespace from left end temporarily 
print(name.strip())        # Removes the whitespace from both ends temporarily 
