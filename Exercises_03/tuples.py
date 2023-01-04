"""
 Script: tuples.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 03 : Tuples
 Tested: Python v3.10.7; Windows 11
 Alpha version: 5th October 2022
"""

newTuple = ("new", "exercise", "tuples", "new")
print(newTuple)

#getting index of elememt
print("Position of 'exercise' :", newTuple.index("exercise"))

#printing specific element in tuple
print(newTuple[2])

#getting count of specific element in typle
print("Count of 'new'  :", newTuple.count("new"))

#Printing Type of variable
print(type(newTuple), "\n")