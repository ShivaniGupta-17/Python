"""
 Script: student budget.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 01: Working with format method
 Tested: Python v3.10.7; Windows 11
 Alpha version: 4th October 2022
"""

print("Student budget")

#All figures monthly
balance=1000

#€2.40 coffee, weekdays, 4 week per month
coffee=2.5 * 5 * 4

#fuel €50 per week, 4 week per month
fuel=50 * 4

print(f"Available income per month is €{balance}.")
print("Total expenditure per month is €{e:1.2f}.".format(e=coffee+fuel))
print("Balance left is €{b:1.2f} each month.".format(b=balance-coffee-fuel))