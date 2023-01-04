"""
 Script: oo1.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 27th October, 2022
 
 Simple class, by convention, use camel case to name classes
"""

#creating a class
class SgClass():
    #constructor: called when instance of class is created
    def __init__(self, greetings):
        print("Running constructor for SgClass")
        #creating attributes and set initial values
        self.message = greetings
    
    def my_method(self):
        print(self.message)

#instance 1
my_class1 = SgClass("Good Day SG!")
my_class1.my_method()
print(type(my_class1))

#instance 2
MyClass2 = SgClass("This is 2nd instance of class.")
MyClass2.my_method()