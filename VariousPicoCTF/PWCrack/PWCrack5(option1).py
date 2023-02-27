import subprocess
import os 
#for coolness: try and make a windows notification pop up when flag was found.  
#This code is not feasable because if I change the range to the whole file it will take forever to attempt each password 

my_list = []

with open("dictionary.txt", "r") as temp_file: 
   lines = temp_file.readlines()
   for i in range (38270, 38279): #change to split up the ranges 
       my_list.append(lines[i].strip())

for password in my_list: 
    send_it = "echo {x} | python3 level5.py"
    proc= subprocess.Popen([send_it.format(x=password)], stdout = subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    flag = out.decode().strip()
    print(flag)
