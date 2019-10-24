# Homework 
This homework consists of three parts. You have roughly a week to complete them. 

## Exercise 1
You are designing a new database for our library. The database must capture the following model. 

The library has many books, and for each book there may be multiple copies. Each copy is identified by the
book ISBN number, and by a copy number. A copy also has a specific location on the shelf.  Every book has a
unique ISBN, a publication year, a title, an author, and a number of pages. Books are published by publishers.
A publisher has a name as well as a location.  In the library, books are assigned to one or several
categories. A category has a name, and can be a subcategory of another category. A reader provides
her name, city, and date of birth in order to register at the library. Each reader gets a unique reader
number. Readers borrow copies of books. Upon borrowing the return date is stored. 

* [Q1] Create an ER diagram of this library system. Give appropriate cardinality information.

* [Q2] Translate the diagram into relations.  

## Exercise 2
Given the following relations

**Course**(<ins>**dept, number**</ins>, course_name)

**Instructor**(<ins>**uid**</ins>, user_name)

**Teaches**(<ins>**uid, dept, number**</ins>)

Write the relational algebra expressions for the following.

* [Q1] Find the courses that are taught by neither Anh Dinh or Cyrille Jegourel 


## Exercise 3
Given the following relations

**Supplier**(<ins>**sid**</ins>, sname, saddress)

**Part**(<ins>**pid**</ins>, pname, color)

**Catalog**(<ins>**sid, pid**</ins>, price)

Write the relational algebra expressions for the following.

* [Q1]. Find name of suppliers who supply some red parts. 

* [Q2]. Find name of suppliers who supply some red and some blue parts. 

* [Q3]. Find id of the parts supplied by at least two different suppliers. 

One operator you may find useful for this exercise is *rename*. <img
src="http://latex.codecogs.com/png.latex?\rho(A, B)"/> renames relation B to A. 

## Exercise 4
Take a look at `flights.zip` that contains a small dataset from the [Bureau of Transportation
Statistics](http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). 

### Loading data
Create and load the following tables from the given dataset

**flight**(fid, year, month_id, day_of_month, day_of_week_id, carrier_id, flight_num, origin_city, origin_state, dest_city, dest_state, departure_delay, taxi_out, arrival_delay, cancelled, actual_time, distance)

**carrier**(cid, name)

**months**(mid, month)

**weekdays**(did, day_of_week)

The primary keys for these tables are fid, cid, mid, and did, respectively. 

### Queries
Write SQL queries for the following.

* [Q1]. Find distinct flight numbers for flights from Seattle WA to Boston MA, operated by Alaska Airlines Inc on Monday.

* [Q2]. Find the top 3 days of the week with the longest average arrival delay. Print name of the day, and average delay.

* [Q3]. Find the names of airlines that operate more than 1000 flights per day. 

* [Q4]. Find the total departure delay per airline over the entire dataset. Print out airline name and the delay. 

* [Q5]. Find airlines that have flights out of New York and have cancelled more than 0.5% of the time. List in ascending order of the percentage. 
## Submission Guide
**Deadline is 23.59pm, 1st November 2019. No late submission.** 

What to submit:
* `submission.pdf` file that contains your answers to exercise 1, 2, 3.

* `create-tables.sql` file that loads the database from the `.csv` files.

* `queries.sql` that contains all the queries.

The two `.sql` files will be run directly on a local MySQL database. Make sure they do not have any syntax
errors. You can test them on your local machine by running: `mysql -u root -b <database_name>  <  create-tables/queries.sql`
