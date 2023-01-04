"""
 Script: maplambda.py
 By: L00171176
 Purpose: Working on map and lambda functions
 Tested: Python v3.10.7; Windows 11
 Alpha version: 8th October 2022
"""

def double(n:int)->int:
    """
    Function to double the value of argument.
    Int is passed and returned.
    """
    return n+n

numbers=[1,2,3,4,5]

#map() use to iterate through objects
result=map(double,numbers)
print(list(result))

#iterating through in loop
for item in map(double,numbers):
    print(item)

#lambda to get radius of circle
cirmf=lambda radius: 2*3.142*radius
area=lambda radius: 3.142*radius*radius
radius = 3
print(f"radius: {radius}; circumferemce: {cirmf(radius)}; area: {area(radius)}")

#understanding scope
string="global"

def scope_fn():
    string="enclosing"
    def nested_fn():
        string="local"
        print(string)
    nested_fn()
    return string

print(scope_fn())
print(string)

#making variable global
newString="global"

def func():
    global newString
    print(f"Current string: {newString}")
    newString="mangled"

func()
print(f"New string: {newString}")