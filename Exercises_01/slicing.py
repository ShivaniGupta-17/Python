"""
 Script: slicing.py
 By: Shivani Gupta (L00171176)
 Description: Walkthrough 01: Escape sequences
 Tested: Python v3.10.7; Windows 11
 Alpha version: 8th October 2022
"""

#slicing a string
a = "Greetings!"
print(a)

#printing first 4 letters
print(f"First 4 letters: {a[0:4:1]}")

#printing last 4 letters
print(f"Last 4 letters: {a[-1:-5:-1]}")

#printing 6th letters
print(f"6th letter: {a[5]}")

#reassemble a new string
b='Shivani'
first_letters=b[0:3:1]
last_letter=b[-1:-3:-1]
insert_letter='j'
new_name=first_letters+insert_letter+last_letter
print(f"Old string: {b} , inserted letter: {insert_letter}")
print(f"New string: {new_name}")

#String Interpolation
name="Shivani"
print(f"Old string: {name}")
name = name[0:4:1] + "T" + name[4:]
print(f"New string: {name}")