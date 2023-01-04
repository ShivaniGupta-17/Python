"""
 Script: func.py
 By: L00171176
 Purpose: Working on Functions, passing and returning values
 Tested: Python v3.10.7; Windows 11
 Alpha version: 8th October 2022
"""

#function to calculate circumference of circle
def circumference(radius=1)->float:
    """
        Calculation the circumference of circle by taking it's radius.
        Default radius=1 if no value is provided.
        Return float value.
    """
    return 2*3.142*radius

#Getting radius as input as string
r=input("Provide a value for radius of circle: ")

#Convert radius from string to float
rf=float(r)

#Circumference function call
cir=circumference(rf)

print(f"Radius = {r}, Circumference = {cir:1.3f}")

#passing unknown no of arguments to function
def adder(*numbers: int)->int:
    """
        Calculation the sum of all values provided as arguments.
        Integer type values is passed in argument.
        Return integer value.
    """
    final=0
    for number in numbers:
        final += number
    return final

print(f"Adding numbers: 12,45,42,6,78 = {adder(12,45,42,6,78)}")

#tuple unpacking
#function iterates through list and find most expensive item
def expensive(prices):
    """
    Iterates through list and find the most expensive item.
    """
    #valiable set up
    maxPrice=0
    maxPriceItem=""
    
    #iterating and unpacking tuple
    for description,price in prices:
        #if prices is maximum then record it in variable
        if price>maxPrice:
            maxPrice=price
            maxPriceItem=description
        #if price is not maximum then do nothing
        else:
            pass
    #return maximumprice and item
    return maxPrice, maxPriceItem

prices=[("Pineapple",0.2),("Apples",.5),("Pears",.7),("Peach",.8)]
#calling function
price,product = expensive(prices)
print(f"List of items : {prices}")
print(f"Maximum price item : {product}, and it's price : {price}")
    