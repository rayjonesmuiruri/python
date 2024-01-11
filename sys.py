#!/usr/bin/py
import sys,socket
while True:
    try:
        user_id = int(input('user_id: '))
        name =  str(input('name: '))
        if user_id  == 0 and name == 'admin':
            print(f"Welcome {name}")
            print("Enter hostname: ")
            try:
                hostname = input()
                ip = socket.gethostbyname(hostname)
                print("The ip is {}".format(ip))
            except socket.gaierror as gaierror:
                gaierror = "wrong host name!!"
                sys.exit(gaierror)
            choice =  input('do you want to exit? ')
            if choice.lower().startswith('y'):
                sys.exit()
            elif choice.lower().startswith('n'):
                continue
            else:
                sys.exit("Invalid Choice !! Exiting")
        else:
            print('you are not root you cant get ip of others')
            sys.exit()
    except  ValueError as verr:
        verr = "you entered wrong values try again!!"
        sys.exit(verr)
    