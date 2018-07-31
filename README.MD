# Log Analysis Project

The project objective is to create a reporting tool that prints out reports (in plain text) based on the data in a database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Environment

A PostGreSql database named **'news'** already exists and includes three tables:

* **authors** - with information about the authors of articles
* **articles** - includes the articles themselves
* **log** - includes one entry for each time a user has accessed the site.

## Reports

The reporting tool will answer the following questions:

* What are the three most popular articles of all time?
* Who are the three most popular authors of all time?
* On which days did more than 1% of requests lead to errors?

## Views:

The following views were added to the database, derived from the log table

#### Note: creates a view of total get requests by day
```
create view gets as
    select time::date as day, count(*) as views from log group by day order by day;
```
#### Note: view from of errors returned from get requests, total by day
```
create view errors as
     select time::date as day, count(*) as views from log where status = '404 NOT FOUND' group by day order by day;
```

## adding views to the database and running the tool:

```
**setting up views**
$ cd <your_path>/vagrant
$ vagrant up
$ vagrant ssh
vagrant:~$ cd/vagrant
vagrant:/vagrant$ psql news
news=> create view gets as
news-> select time::date as day, count(*) as views from log group by day order news-> by day;
news=> create view errors as
news-> select time::date as day, count(*) as views from log where status ='404 news-> NOT FOUND' group by day order by day;

**running the tool**
news=> \q
vagrant:/vagrant$ python <your_path>/news.py
```
