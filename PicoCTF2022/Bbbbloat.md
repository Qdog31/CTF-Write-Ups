# Bbbbloat
- Category : Reverse Engineering	
- Points : 300
- Flag: picoCTF{cu7_7h3_bl047_d059b523}



## Challenge

Can you get the flag? Reverse engineer this binary.

Hint: (None)

## Solve

1) I first tried to `cat` the provided file, but I was just provided with unreadable text.
2) I then realized that they provided me with a binary, so I instantly fired up Ghidra and imported/ opened the file.  
3) Now that the file was open, I had to find where the main function was myself. I went one by one through each function to see if any of them stood out to me. The function `FUN_00101307` stood out because it had 35 lines of code (the most compared to the others) and had:    
```
  if (local_48 == 0x86187) {
    __s = (char *)FUN_00101249(0,&local_38);
    fputs(__s,stdout);
    putchar(10);
    free(__s);
```

The chunk of code stood out because it used an if statement which made me think "if this is true, then do this". I was correct. I then looked down two lines of code and noticed that the function printed something if local_48 ==0x86187.

4) I knew that `0x86187` looked familiar, so I right clicked it, and converted it to decimal right in Ghidra which was `549255`

5) For the solve, I ran the command: `chmod +x bbbbloat` and ran the binary where I was greeted with `Whats my favorite number?`. I inputted the `549255` number and was returned the flag. 

## Thoughts

After getting the flag to this challenge and noticing that it was worth 300 points, I was surprised! I guess everything I learned from a a weekend with Chris Eagle payed off. Anyways, I liked how I had to find the main function myself and how I had to decode the programs favorite number to get the flag. This was a good beginner challenge that allowed me to get more practice in with if and else statements. 
