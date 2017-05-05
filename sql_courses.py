# sql.py - Create a SQLite3 table and populate it with data


import sqlite3
import csv

# create a new database if the database doesn't already exist
with sqlite3.connect('courses.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute('CREATE TABLE IF NOT EXISTS courses(course_id TEXT, course_name TEXT, prereq TEXT, quarter TEXT)')

with open("csCourses.csv") as csv_file:
    for row in csv.reader(csv_file, delimiter = ','):
        c.execute('''INSERT INTO courses VALUES(:course_id, :course_name, :prereq, :quarter)''', row)

connection.commit()
connection.close()
   
