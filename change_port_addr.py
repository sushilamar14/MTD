from random import randrange
import random
import time

a = int(input("enter number between 1 and 255 \t")) #peudo total number of free ports available
list=[] 

for i in range(1000):
    r=random.randint(1,255)
    if r not in list: list.append(r)
    if len(list)==a:
        break
list.sort() #list of all the free ports

t_ports=len(list) #total number of free ports
print ("sorted open ports are",list) #sorting of the list in ascending order
print("total number of open ports= ",len(list)) #printing total numver of free ports 
f=time.time()  #epoch time from time
local_time = time.ctime(f) #local time generator from epoch
print("Local time:", local_time) 

print("epoch time is",f)
ab=(random.randint(1, t_ports))#using epoch as a seed to generate a peudo random number in the range of 1-total available free ports

print("which item to choose from list =",ab,"th")#position of selected port number in list
port=list[ab-1]#removed port number from available port numbers
print("port choosed of list:",port) #selected port number is
