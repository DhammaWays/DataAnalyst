-- SQL Query assignment for Data Analyst Interview parctice project
-- Lekhraj Sharma, Data Analyst Nanodegree from Udacity
-- Table "users"
/*
+-------------+-----------+
| Column      | Type      |
+-------------+-----------+
| id          | integer   |
| username    | character |
| email       | character |
| city        | character |
| state       | character |
| zip         | integer   |
| active      | boolean   |
+-------------+-----------+
*/
-- CREATE TABLE users (id integer, username VARCHAR(20), email varchar(30), city varchar(20), state varchar(20), zip integer, active boolean);
-- Data
/*
insert into users (id, username, email, city, state, zip, active) values 
(1,'alex','alex@gmail.com','San Francisco','California',94101,True),
(2,'burpy','burpy@yahoo.com','San Francisco','California',94102,True),
(3,'cuty','cuty@gmail.com','San Ftrancisco','California',94101,False),
(4,'doug','doug@gmail.com','Los Angeles','California',90001,True),
(5,'ernie','ernie@yahoo.com','Los Angeles','California',90001,False),
(6,'fred','fred@gmail.com','Huntsville','Alabama',35801,True),
(7,'gumpy','gumpy@gmail.com','Freeport','Maine',04032,True),
(8,'henry','henry@yahoo.com','Santa Fe','New Mexico',87500,True),
(9,'ivory','ivory@gmail.com','Austin','Texas',78701,True),
(10,'john','john@gmail.com','Austin','Texas',78702,False),
(11,'jarvis','jarvis@gmail.com','Austin','Texas',78703,True),
(12,'kron','kron@yahoo.com','Cleveland','Ohio',44101,False),
(13,'lilly','lilly@yahoo.com','Logan ','Utah',84321,False),
(14,'mark', 'mark@gmail.com','Cincinnati','Ohio',45201,True);
*/
-- select * from users;
/*
+------+----------+------------------+----------------+------------+-------+--------+
| id   | username | email            | city           | state      | zip   | active |
+------+----------+------------------+----------------+------------+-------+--------+
|    1 | alex     | alex@gmail.com   | San Francisco  | California | 94101 |      1 |
|    2 | burpy    | burpy@yahoo.com  | San Francisco  | California | 94102 |      1 |
|    3 | cuty     | cuty@gmail.com   | San Ftrancisco | California | 94101 |      0 |
|    4 | doug     | doug@gmail.com   | Los Angeles    | California | 90001 |      1 |
|    5 | ernie    | ernie@yahoo.com  | Los Angeles    | California | 90001 |      0 |
|    6 | fred     | fred@gmail.com   | Huntsville     | Alabama    | 35801 |      1 |
|    7 | gumpy    | gumpy@gmail.com  | Freeport       | Maine      |  4032 |      1 |
|    8 | henry    | henry@yahoo.com  | Santa Fe       | New Mexico | 87500 |      1 |
|    9 | ivory    | ivory@gmail.com  | Austin         | Texas      | 78701 |      1 |
|   10 | john     | john@gmail.com   | Austin         | Texas      | 78702 |      0 |
|   11 | jarvis   | jarvis@gmail.com | Austin         | Texas      | 78703 |      1 |
|   12 | kron     | kron@yahoo.com   | Cleveland      | Ohio       | 44101 |      0 |
|   13 | lilly    | lilly@yahoo.com  | Logan          | Utah       | 84321 |      0 |
|   14 | mark     | mark@gmail.com   | Cincinnati     | Ohio       | 45201 |      1 |
+------+----------+------------------+----------------+------------+-------+--------+
*/
-- Query to find the top 5 states with the highest number of active users. Include the number for each state in the query result
select state, count(*) as num_active_users from users where active is True group by state order by count(*) desc, state limit 5;
-- Expected Output
/*
+------------+------------------+
| state      | num_active_users |
+------------+------------------+
| California |                3 |
| Texas      |                2 |
| Alabama    |                1 |
| Maine      |                1 |
| New Mexico |                1 |
+------------+------------------+
*/