"""
 Script: add.py
 By: Shivani Gupta (L00171176)
 Description: Python Walkthrough 01: String functions
 Tested: Python v3.10.7; Windows 11
 Alpha version: 4th October 2022
"""

#string functions
a="I like black coffee"
print(a)

#type of variable
print(type(a),"\n")

#lengeth of string
print("String lengeth = ", len(a))

#Splitting string
print("Splitting:", a.split())

#joining two strings
print("Joining:", ''.join([a.split()[0],a.split()[3]]))

#Index of a letter in string
print("Indexing: ", a.index("ack"))

#finding sequence in string
print("Is 'coffee' in string? ","coffee" in a)

#pringint range of list
print(list(range(0,12,3)))

#Below are examples of a few string functions

#isalnum
print("Is string alphanumeric?\t", a.isalnum())

#isalpha
print("Is string alphabetic?\t", a.isalpha())

#islower
print("Is string in lowercase?\t", a.islower())
print(a.split()[3] + " - islower?\t", a.split()[3].islower())

#lower
print("Converting to lowercase:", a.lower())

#isupper
print("Is string in uppercase?\t", a.isupper())

#upper
print("Converting to uppercase:", a.upper())

#istitle
print("Is string titlecases?\t", a.istitle())

#title
print("Title caseing string:\t", a.title())

#swapcase
print("Swapping case:\t", a.swapcase())

#removeprefix
print("Removing prefix 'I like':", a.removeprefix('I like'))

#removesuffix
print("Removing suffix 'coffee':", a.removesuffix('coffee'))
