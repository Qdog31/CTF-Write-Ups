# where are the robots  (PicoCTF)
- Category : Web Exploitation 
- Points : 100 
- Flag: picoCTF{ca1cu1at1ng_Mach1n3s_477ce}


## Challenge
Can you find the robots? https://jupiter.challenges.picoctf.org/problem/36474/ (link) or http://jupiter.challenges.picoctf.org:36474

## First Steps
First, I clicked on the link to check out the website. After that, I used prior knowledge from my CY105 to check out the /robots.txt directory of the website. I knew that this would contain information that the site didn't want google to crawl. 

## Solve
After navigating to /robots.txt, the screen displayed: 
"User-agent: *
Disallow: /477ce.html

After seeing that it disallowed that directory, I navigated to that directory to see waht it contained. After going to that directory, the screen displayed the flag with the message "I guess you found the robots." 

## Thoughts
I really liked this challenge and for someone who didn't have prior knowledge on web stuff, It was good to learn about crawling and how google actually searches for information on the world wide web. 