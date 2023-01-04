"""
 Script: my_for.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 04: For Loops
 Tested: Python v3.10.7; Windows 11
 Alpha version: 6th October 2022
"""

iterable_variable=[1,2,3,4,5,6]

#iteating elements in for-loop
for item in iterable_variable:
    print(item)
print("\n")

#arithmetic operation on iteration of for-loop
total=0
for item in iterable_variable:
    total+=item
print(total)

#if condition in for-loop
for item in iterable_variable:
    if item%2!=0:
        print(item, end="; ")
print("\n")

for letter in "Shivani Gupta":
    if letter == "v":
        print(f"Found letter {letter}")
        break
    else:
        print(f"Don't want {letter}")

#example for pass, continue, break
newList=[1,8,3,9,6]
for number in newList:
    if number==1:
        pass
    if number==2:
        continue
    if number==3:
        print(f"Found number {number}")
    if number==0:
        break

#example for range
for index in range(1,100,5):
    print(index, end=",")
    
#printing items of tuple
tuples=[(1,2),(3,4),("A","B")]
for items in tuples:
    print(items)

#tuple unpacking
for a,b in tuples:
    print(a,"\t",b)
