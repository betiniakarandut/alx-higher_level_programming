#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(user=username, passwd=password,
                         db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
