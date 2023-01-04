"""
 Script: library2.py
 By: Shivani Gupta (L00171176)
 Description: Python Walkthrough 06: Libraries
 Tested: Python v3.10.7; Windows 11
 Alpha version: 9th October 2022
"""

from math import sqrt
print("Enter length of 2 sides for a triangle:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse to three decimal places is: {hyp:1.3f}".format(hyp=c))