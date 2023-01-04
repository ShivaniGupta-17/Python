"""
 Script: exercise.py
 By: L00171176
 Purpose: Exercise on functions
 Tested: Python v3.10.7; Windows 11
 Alpha version: 8th October 2022
"""

#to get value 'True'
def divisible(numerator:int, denominator:int)->bool:
    return numerator%denominator==0

print(divisible(30,3))

#to get value 'False'
def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        return iterate_number==number

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

#function to search for an even number in a list of numbers
def findEvenNo(numberList:list)->bool:
    for iterate_number in numberList:
        if iterate_number%2==0:
            return iterate_number%2==0
            break

listno=[7,2,4,6,5]
print(findEvenNo(listno))

#lambda function to calculate the volume of a cylinder
radius=4
height=8

vol=lambda vol_cy_r: 3.142*radius*radius
volc=lambda vol_cy_h: vol(radius)*height

print(f"Volume of cylinder with radius {radius} and height {height} = {volc(height)}")