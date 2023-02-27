# SQL Direct
- Category : Web Exploitation 	
- Points : 200
- Flag: picoCTF{L3arN_S0m3_5qL_t0d4Y_472538a0}



## Challenge

Connect to this PostgreSQL server and find the flag! psql -h saturn.picoctf.net -p 56634 -U postgres pico Password is postgres

Hints: What does a SQL database contain?

## Solve

1) I connected to the PostgreSQL server with the provided credentials.
2) I attempted to use linux commands like cat and ls, but had no luck 
3) I then looked at the provided hint and realized tht I would have to try and query a table. I researched how to query a table and used the following website: https://flaviocopes.com/postgres-how-to-list-tables-database/

4) I used the commmand `\dt` to list all the tables. I noticed that there was only one named `flags`.
5) Knowing that there was a table names `flags`, I researched how to make queries on this table. 

6) For the solve, I inputted  `SELECT * FROM flags;` and got the flag following output: 

```
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_472538a0}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)
```


## Thoughts

Although a simple challenge, it took me a while to figure out exactly what I needed to do (approximately forty minutes). I knew that a SQL database contained tables, but I was unsure of how to access these tables. The only thing I could figure out how to do at first, was list the tables. But, after a lot of research and realizing that I had to input the commands one line at a time, I got the flag with no issues. 






