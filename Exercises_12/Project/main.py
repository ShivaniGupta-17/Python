"""
 Script: main.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 2nd November, 2022
"""

from Source.checkOS import detect_os, detect_working_directory
print(detect_os())
print(detect_working_directory())