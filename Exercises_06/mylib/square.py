"""
 Script: square.py
 By: Shivani Gupta (L00171176)
 Description: Python Walkthrough 06
 Tested: Python v3.10.7; Windows 11
 Alpha version: 9th October 2022
"""

square_text = "Yo, time to square stuff!"
def square(x):
    return x*x

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")