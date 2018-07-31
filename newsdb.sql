import news.py

# create view of all get requests, by date
create view gets as
    select time::date as day, count(*) as views from log group by day order by day;

# create view where get requests returned an HTTP 404 error
create view errors as
     select time::date as day, count(*) as views from log where status = '404 NOT FOUND' group by day order by day;

