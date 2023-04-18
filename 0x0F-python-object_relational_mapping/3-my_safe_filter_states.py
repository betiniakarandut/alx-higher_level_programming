#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, safe from MySQL injections
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    # Create cursor to execute queries
    cur = db.cursor()

    # Get the state name to search for and sanitize it
    state = MySQLdb.escape_string(sys.argv[4])

    # Execute SQL query with sanitized input
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id",
                (state,))

    # Fetch all rows and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
