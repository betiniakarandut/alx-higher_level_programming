#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to database
    db = MySQLdb.connect(
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost'
                        )
    cursor = db.cursor()

    # Execute query
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Print results
    for row in cursor.fetchall():
        print(row)

    # Close connection
    cursor.close()
    db.close()
