"""
 Script: dict.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 03 : Dictionaries
 Tested: Python v3.10.7; Windows 11
 Alpha version: 5th October 2022
"""

newDitionary = {"FName":"Shivani", "SName":"Gupta", "University":"ATU Donegal", "Country":"India"}

print(newDitionary,"\n")

#Extracting specific information
print(newDitionary["University"],"\t",newDitionary["Country"])

#adding to dictionary
newDitionary["course"]="MSc Cloud - IaC"
print(newDitionary)

#changing value of specific key
newDitionary["course"]="MSc Cloud"
#print(newDitionary)

#getting all keys
print(newDitionary.keys())

#getting all values
print(newDitionary.values())

#getting all items
print(newDitionary.items())