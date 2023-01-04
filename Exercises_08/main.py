"""
 Script: main.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 29th October, 2022
"""

"""
calling calss for devices.py
"""

from devices import Firewall, Switch, LoadBalancer

#Firewall instance
firewall28=Firewall("firewall28")
#configure
firewall28.configure_firewall()
#verify crc
firewall28.calc_crc("data")

#Switch instance
switch23=Switch("switch23")
#configure
switch23.configure_switch()
#verify crc
switch23.calc_crc("data")

#Load Balancer instance
loadbalancer31=LoadBalancer("loadbalancer31")
#configure
loadbalancer31.configure_load_balancer()
#verify crc
loadbalancer31.calc_crc("data")