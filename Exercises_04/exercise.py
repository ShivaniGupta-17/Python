"""
 Script: exercise.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 04 : Loop on Dictionaries
 Tested: Python v3.10.7; Windows 11
 Alpha version: 6th October 2022
"""

#Walkthrough - 4; Exercise
scan={"192.168.3.10":"80","192.168.3.11":"443","192.168.3.55":"22"}

print(scan)
print(scan.items())

for ipv4,port in scan.items():
    print(f"Found a service on {ipv4} at {port}")