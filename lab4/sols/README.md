# Lab 4 - Relational Algebra and SQL 

This lab contains exercises on querying databases. Some recaps:

* Relational algebra: compose operators, such as selection, projection, join, etc. into complex queries. 

* SQL: use MySQL syntax to express queries. Reminder: SQL uses **bag abstraction**, not set!

## Exercise 1
Given the following table which records the results of running competition at the Asian Game 2019. 

**Run**(<ins>**Name, Distance**</ins>, Time)

Give an expression in relational algebra that finds all runners who only participate in 100m category. 

## Exercise 2
Given the following tables that capture a library database:

**Reader**(<ins>**ReaderNo**</ins>, Name, City, DoB)

**Book**(<ins>**ISBN**</ins>, Title, Author, NoPages, PubYear, PubName)

**Publisher**(<ins>**PubName**</ins>, PubCity)

**Category**(<ins>**CategoryName**</ins>, Description)

**BookCategorty**(<ins>**ISBN, CategoryName**</ins>)

**Loan**(<ins>**ReaderNo, ISBM, Copy**</ins>, ReturnDate)

Give expressions in relational algebra for the following:

* [Q1] Find books in category Humor but not in category Crime

* [Q2] Find readers who borrowed books that were published in their cities. 

## Exercise 3

MySQL does not support set intersection (slide 24 in Week 2 (SQL 1) is not correct. EXCEPT is supported in
SQLite). 

How do you implement R(<ins>**a**</ins>) - S(<ins>**a**</ins>) ?

(Hint: nested query is useful here!)

## Exercise 4
Load the bike sharing dataset from lab2 to MySQL. Write queries to answer the following. 

* [Q1] Count the number of cities (no duplicates)

    `select count(distinct(city)) from station;`

* [Q2] Count the number of stations in each city. Output the city name, and station count. 

  `select city, count(station_id) as cnt from station group by city order by cnt desc;`

* [Q3] Count the number of self-loop trips. A self-loop trip is one that starts and ends at the same station.

  `select count(*) as cnt from trip where start_station_id = end_station_id;`

* [Q4] Print the ratio of self-loop trips over all trips. 
  Hint: you can use nested queries, or create temporary table. Syntax for the latter is: `create temporary
  table <name> <SQL query>`
  ```
  select self_loop_cnt.cnt * 1.0 / trip_cnt.cnt as percentage
       from (
            select count(*) as cnt
            from trip
            where start_station_id = end_station_id
      ) as self_loop_cnt,
      (
        select count(*) as cnt
        from trip
      ) as trip_cnt;
  ```

  or:
  
  ```
  create temporary table t1 select count(*) as cnt from trip where start_station_id = end_station_id;
  create temporary table t2 select count(*) as cnt from trip;
  select t1.cnt * 1.0 / t2.cnt as percentage from t1, t2;
  ```

* [Q5] Find the percentage of trip in each city, sorted by descending order of the percentage. Print out the
city name, and percentage of trips belonging to this city. A trip belongs to a city if it starts or ends in
this city. If it starts and ends in the same city, only count this trip once.  

  ```
  create temporary table t1 select city, count(distinct(id)) as cnt
    from trip, station
    where station_id = start_station_id or station_id = end_station_id
    group by city;

  create temporary table t2 select count(*) as cnt from trip;

  select city, t1.cnt * 1.0 / t2.cnt as ratio from t1, t2;
  ```

* [Q6] Find the most popular city, in terms of percentage of trips belonging to the city. 

* [Q7] Find all the bikes (their `bike_id`) that have been to more than 1 city. A bike has been to a city if
its start and end station of one of its trips is in this city. Order by the city count, descending.  

   ```
   select bike_id, count(distinct(city)) as cnt 
   from trip, station 
   where start_station_id = station_id or end_station_id = station_id group by bike_id 
   having count(distinct(city)) > 1
   order by cnt desc;
   ```
* [Q8] List the bikes (their `bike_id`) that have never been to `Japantown` station. 

  ```
  create temporary table t1 select bike_id from trip 
  where start_station_name = "Japantown" or end_station_name="Japantown" group by bike_id;

  create temporary table t2 select distinct(bike_id) from trip;

  select * from t2 where bike_id not in (select * from t1);
  ```
