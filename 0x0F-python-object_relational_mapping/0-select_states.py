#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    # Fetch all rows as a list of tuples
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connections
    cursor.close()
    db.close()

