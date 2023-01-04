"""
 Script: list_comp.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 04: List Comprehensions
 Tested: Python v3.10.7; Windows 11
 Alpha version: 7th October 2022
"""

newList=[]
new_String="Python is interesting."

#characters of string as elements in list
for letter in new_String:
    newList.append(letter)
print(newList)

#collapsing code into single statement
newList=[letter for letter in new_String]
print(newList)

#range in list
newList=[number for number in range(0,15)]
print(newList)

#if-condition in list allocation
newList=[number*10 for number in range(0,15) if number<8]
print(newList)

#converting depth from deet into meters
conversion=0.3048
depthInFeet=[12.3,13.8,15.3,12.1,8.8]
depthInMeters=[depth*conversion for depth in depthInFeet]
print(depthInMeters)