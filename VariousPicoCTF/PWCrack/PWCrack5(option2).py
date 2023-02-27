import hashlib
import os 
#got code from github for testing 

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

dictionary = open("dictionary.txt", "r").readlines()
for word in dictionary:
    word = word.strip()
    if hash_pw(word) == correct_pw_hash:
        print("Password is:", word)

send_it = "python3 level5.py"
os.system(send_it)