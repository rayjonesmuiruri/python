#!/usr/bin/env python3
import socket 
def print_machine_info():
    #call the gethostname() method from the socket library
    hostName = socket.gethostname()
    #call the gethostbyname() method and pass in the hostName as an argument
    ip_address = socket.gethostbyname(hostName)
    #print the host name
    print("Hostname: {}".format(hostName))
    #print the ip address
    print("Ip: %s" %ip_address)
#call the print_machine_info function
if __name__ == '__main__':
    print_machine_info()
    