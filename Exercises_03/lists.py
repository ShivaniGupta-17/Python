"""
 Script: lists.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 03 : Lists
 Tested: Python v3.10.7; Windows 11
 Alpha version: 5th October 2022
"""

#creating new list
newList=[1,2,4,"A","B"]
print("1st list  =", newList)

#printing no of elements in list
print("no of elements  =", len(newList))

#append element to the end of list
secondList.append("added word")
print("Appended list  =", secondList)

#insert am element at specific position in list
newList.insert(3,"X")
print("Insert to 1st list =", newList)

#concatenate two list together
secondList=[8,"S","T",8,"word"]
print("2nd list   =", secondList)

print("Concatenating both list =", newList+secondList)

#printing nested list, ie list of list
print("Nested list (list of list)=", [newList,secondList])

#changing element of list
secondList[4]="new word"
print("Changed 2nd list =", secondList)

#extend the list by 1 or more elememts
newList.extend([6,10,"V"])
print("Extend 1st list  =", newList)

#removing an element from list
newList.remove("A")
print("Removing element 'A' =", newList)

#slicing list [start, stop, step]
print(newList[1:5:2])

#getting an element from list
print("3rd element of list =", newList[2])

#pop the last element
print("Pop element  =", secondList.pop(),"\n 2nd list =",secondList)

#count the repetation of specific element
print("Repetations of '8' =", secondList.count(8))

#reverse the order of elements inside list 
secondList.reverse()
print("Reversed 2nd list =", secondList)