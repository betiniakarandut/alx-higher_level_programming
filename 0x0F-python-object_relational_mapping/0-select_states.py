#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
                         host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[30]
                        )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to select all states sorted in ascending order by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close database connection
    db.close()
