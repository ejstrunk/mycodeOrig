#!/usr/bin/python3
import netifaces

ans = input(f"Please select from the follow interfaces: \n{netifaces.interfaces()}: ").lower

if ans == "lo":
    print('\n**************Details of Interface - ' + netifaces.interfaces + ' *********************')
    print('MAC: ', end='')
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # prints the MAC address
    print('IP: ', end='')
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # prints the IP address
else
