from random import randrange
import random
import time

a = int(input("enter number between 1 and 255 \t")) #total number of free ports
list=[]

for i in range(1000):
    r=random.randint(1,255)
    if r not in list: list.append(r)
    if len(list)==a:
        break
list.sort() 

t_ports=len(list)
print ("sorted open ports are",list)
print("total number of open ports= ",len(list))
f=time.time()  #epoch
local_time = time.ctime(f)
print("Local time:", local_time)

print("epoch time is",f)
random.seed(f) 
ab=(random.randint(1, t_ports))

print("which item to choose from list =",ab,"th")
port=list[ab-1]
print("port choosed of list:",port)