# Quintin Sherrod
- Category : Forensics 
- Points : 250
- Flag: MetaCTF{cleartext_private_pgp_keys}

## Challenge

"Caleb was designing a problem for MetaCTF where the flag would be in the telnet plaintext. Unfortunately, he accidentally stopped the packet capture right before the flag was supposed to be revealed. Can you still find the flag? "


## Solve

We were given a PCAP file, so I started by opening it up. After opening the file, I went to Statistics (at the top of the page), then Conversations, and three TCP3 files popped up. I went through each of them with the Fallow Stream button on the bottom of the screen. Within these streams, we have the PGP Message, PGP Private key, and another page that has useful information such as the passphrase. 

Then, using this information, we can go to CyberChef and use the PGP Decrypt operation. Then, we input the given Private Key and private key passphrase, and the message.asc file (we got this file from downloading it from the TCP stream). After the information is in, we you can click the magic wand to gunzip the output into a readable flag. 

Extra Notes: Before realizing I could use CyberChef, I learned about the linux commands to add the private key to my keychain. I used gpg –import key.gpg to import the key, then I did gpg –decrypt message.asc > plain.txt which gave me a file that was still compressed/ not readable. Although I did not need to do this to solve the flag, it was still good to learn about gpg in general. 


## Thoughts

This challenge wasn't too bad, but I was overthinking it way too much. I was trying to use linux commands in order to add the private key to my keychain and do all of these different things. One of the things that I learned is that sometimes utilizing the discord - is useful. 
