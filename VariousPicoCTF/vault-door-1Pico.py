# Created by Quintin Sherrod 
# Challenge vault-door-1 (pico gym)
# Points: 100 
# February 25 2023 

dic = {}

with open ("VaultDoor1.java","r") as temp_file: 
    for i in range(23): # removes useless lines that doesn't contain flag values 
        temp_file.readline()

    for line in temp_file:
        position = line[31:33]
        position = position.replace(")", "") # gets rid of the parenthesis if number is only 1 digit
        value = line[39:40]
        dic.update({position:value})
        #print(position,value) correct position in list with its respective value 

dic.update({position:value})
del dic[""] # deletes the empty kv pair I was having issues with 
#print(dic) check proper k,v pairs

flag = []
for key,value in sorted(dic.items(), key=lambda item: int(item[0])): # orders dictionary from 0-31
    flag.append(value)

flag_content = "".join(flag)
full_flag = "PicoCTF{{{value}}}" #pico flag contains curly brackets and so we need two more pairs for a format string.

print(full_flag.format(value=flag_content))
    
    
    

        
