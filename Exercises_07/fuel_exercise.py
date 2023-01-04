"""
 Script: fuel_exercise.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 27th October, 2022
"""

def fuel_endurance(fuel,fuel_consumption):
    try:
        endurance=fuel/fuel_consumption
        print(f"Endurance: {endurance}")
    except ZeroDivisionError:
        print("Motor is idling, flow meter cannot calculate fuel flow")

fuel=int(input("Enter fuel in liters: "))
fuel_consumption=int(input("Enter fuel consumption in liters per minutes: "))

fuel_endurance(fuel,fuel_consumption)