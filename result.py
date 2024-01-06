#!/usr/bin/env python3
num1 =  int(input())
num2 = int(input())
result = 0 
iterations = 0
rangE = int(num1/num2)
for iterations in range(rangE):
    result = num1 - num2
    num =  result 
    iterations += 1
    if result == 0:
        break
print("{} enters {} {} times".format(num2,num1,iterations))
    