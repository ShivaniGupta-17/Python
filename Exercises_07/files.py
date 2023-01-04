"""
 Script: files.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 27th October, 2022
"""

filename="logfile.txt"

try:
    with open(filename, "r") as file_handle:
        print(f"Writing a test line to {filename}")
        file_handle.write("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
finally:
    print("Finishing up!")
    #close not needed when using with statement
    #file_handle.close()
