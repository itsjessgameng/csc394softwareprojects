import sqlite3

conn = sqlite3.connect('projectdb.db')
c = conn.cursor()

#CREATE TABLES USED IN THE DATABASE
c.execute('CREATE TABLE IF NOT EXISTS students(id INTGER, last_name TEXT, first_name TEXT, major TEXT, concentration TEXT, PRIMARY KEY(id))')
c.execute('CREATE TABLE IF NOT EXISTS courses(course_id INTGER, course_name TEXT, pre_req TEXT, quarter_ava TEXT, PRIMARY KEY(course_id))')
c.execute('CREATE TABLE IF NOT EXISTS classestaken(id INTGER, course_id INTGER, FOREIGN KEY(id) REFERENCES students(id), FOREIGN KEY(course_id) REFERENCES courses(course_id))')
c.execute('CREATE TABLE IF NOT EXISTS faculty(id INTGER, last_name TEXT, first_name TEXT, PRIMARY KEY(id))')
c.execute('CREATE TABLE IF NOT EXISTS admin(id INTGER, last_name TEXT, first_name TEXT, PRIMARY KEY(id))')
c.execute('CREATE TABLE IF NOT EXISTS logininfo(id INTGER, username TEXT, password TEXT, PRIMARY KEY(username))')

conn.commit()