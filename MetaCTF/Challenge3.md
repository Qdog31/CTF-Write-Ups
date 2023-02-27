# Quintin Sherrod 
- Category : Reconnaissance
- Points : 200
- Flag: CVE-2021-34527

## Challenge

"Malicious operators typically exploit unpatched vulnerabilities within target environments to gain initial access, escalate privileges, and more. What recent vulnerability have Conti ransomware operators exploited to run arbitrary code with SYSTEM privilege? 
The flag format will be CVE-XXXX-XXXXX" 

## Solve

I stumbled upon a bunch of cites and eventually landed on https://us-cert.cisa.gov/ncas/alerts/aa21-265a . Once on the site, I found the “PrintNightmare” vulnerability with the fallowing CVE code: CVE-2021-34527.

## Thoughts 

This challenge took me 30 minutes to figure out because of two reasons. 1) I did not look at the title of the challenge carefully, and 2) I did not understand the format of the CVE flag.Before figuring out how to find the flag, I had to look up the format for CVE’s and found the below information: CVE-2021-34527.
The text chunk is the same for all CVE’s, the second chunk is the year, and the third chunk is the serial number for the specific vulnerability. 

