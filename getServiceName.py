#!/usr/bin/env python3
#if you know the port number of a network you can find its service name
import socket
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print("Port {} => service name: {}".format(port, socket.getservbyport(port, protocolname)))
        #example
    print("Port {} => service name: {}".format(53, socket.getservbyport(53,'udp')))
        
if __name__ == '__main__':
    find_service_name()
#http , smtp , domain are services and are running on port 80, 25 and 53 respectively

