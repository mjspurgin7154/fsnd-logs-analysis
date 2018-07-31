#! /usr/bin/python3.6
#
''' news.py -- implementation of a internal reporting tool
    that will use information from the database to discover
    what kind of articles the site's readers like.'''
#
import psycopg2
import math


def connect(database_name="news"):
    """ Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Connection not established")


def getArticles():
    """ returns the three most viewed articles in the db"""
    db, cursor = connect()
    top_titles = (
        "select title, count(*) as views from log join articles \
        on log.path = concat('/article/', articles.slug) group by title \
        order by views desc limit 3;")
    cursor.execute(top_titles)
    print("")
    print("What are the three most popular articles of all time?")
    print("")
    for (title, views) in cursor.fetchall():
        print("    {} - {} views".format(title, views))
    print("")
    print("-" * 70)
    db.close()


def getAuthors():
    """ returns the three most viewed authors in the db"""
    db, cursor = connect()
    top_authors = ("select authors.name, count(*) as views from authors, articles, log \
       where authors.id = articles.author and log.path = concat('/article/', \
       articles.slug) group by authors.name order by views desc limit 3;")
    cursor.execute(top_authors)
    print("")
    print("Who are the three most popular authors of all time?")
    print("")
    for (name, views) in cursor.fetchall():
        print("    {} - {} views".format(name, views))
    print("")
    print("-" * 70)
    db.close()


def getErrors():
    """ returns the days where over 1% of requests led to errors"""
    db, cursor = connect()
    errors = ("select errors.day, (errors.views::float/gets.views * 100)\
        ::numeric(3, 2) as  pct from errors join gets on errors.day = \
        gets.day;")
    cursor.execute(errors)
    print("")
    print("On which days did more than 1% of requests lead to errors?")
    print("")
    for (day, pct) in cursor.fetchall():
        if pct > 1.0:
            print("    {:%B %d, %Y} - {}% errors".format(day, pct))
    print("")
    db.close()


if __name__ == '__main__':
    getArticles()
    getAuthors()
    getErrors()
