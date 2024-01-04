#!/usr/bin/env python3 
import socket
from binascii import hexlify
remoteName = str(input("Enter host name: "))
ip_address = socket.gethostbyname(remoteName)
choice = str(input("Do you want to unpack the Ip Address?(y or n): "))
def main():
    upack()
def upack():
    if choice == 'y':
        packed = socket.inet_aton(ip_address)
        unpacked = socket.inet_ntoa(packed)
        print("Ip -> {} Packed ip -> {} Unpacked ip -> {}".format(ip_address,hexlify(packed), unpacked))
    else:
        print("The ip address of {} is {}".format(remoteName, ip_address))
if __name__ == '__main__':
    main()