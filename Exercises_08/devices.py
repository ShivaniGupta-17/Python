"""
 Script: devices.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 29th October, 2022
"""

"""
Parent Class for Devices
"""
class Device():
    #class object
    pi=3.142
    
    #constructor call
    def __init__(self)->None:
        print("Running Constructor for base class.")
        #attributes
        self.debug=False
    
    #abstract class NotImplementedError
    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate.")
    
    #calculating CRC
    def calc_crc(self, frame:str)->int:
        print("Checking CRC from base")
        crc=16987432
        return crc

"""
Child Class for Switches
"""

class Switch(Device):
    #constructor call
    def __init__(self,param1)->None:
        
        #call to parent class
        Device.__init__(self)
        print(f"Running constructor for {param1}")
        
        #attributes
        self.param1=param1
        self.test_msg=""
    
    def configure_switch(self):
        print("Configuring Switch")
    
    def calc_crc(self, frame:str)->int:
        print("Checking CRC from Switch")
        crc=16987432
        return crc

"""
Child Class for Firewalls
"""

class Firewall(Device):
    #constructor call
    def __init__(self,param1)->None:
        
        #call to parent class
        Device.__init__(self)
        print(f"Running constructor for {param1}")
        
        #attributes
        self.param1=param1
        self.test_msg=""
    
    def configure_firewall(self):
        print("Configuring Firewall")
    
    def calc_crc(self, frame:str)->int:
        print("Checking CRC from Firewall")
        crc=16987432
        return crc

"""
Child Class for Load Balancers
"""

class LoadBalancer(Device):
    #constructor call
    def __init__(self,param1)->None:
        
        #call to parent class
        Device.__init__(self)
        print(f"Running constructor for {param1}")
        
        #attributes
        self.param1=param1
        self.test_msg=""
    
    def configure_load_balancer(self):
        print("Configuring Load Balancer")
    
    def calc_crc(self, frame:str)->int:
        print("Checking CRC from Load Balancer")
        crc=16987432
        return crc
