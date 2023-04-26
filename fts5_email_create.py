#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('email.db')
print ("Opened database successfully")

conn.execute('''CREATE VIRTUAL TABLE email USING fts5(sender, title, body);''')
print("Table created successfully")

conn.close()