"""
 Script: oo2.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 27th October, 2022
"""

class MyTemplate():
    #define class object attribute, same for all instance
    class_obj_att1 = 6378137
    class_obj_att2 = 6356752
    
    #constructor call
    def __init__(self, attrb1:str, attrb2:bool) -> None:
        print("Constructor ran.")
        #assign argument to attribute
        self.attr1=attrb1
        self.attr2=attrb2

#instantiate class
my_obj = MyTemplate("SG",True)

#check object and type
print(type(my_obj))

print(my_obj.attr1, my_obj.attr2)

print(my_obj.class_obj_att1, my_obj.class_obj_att2)