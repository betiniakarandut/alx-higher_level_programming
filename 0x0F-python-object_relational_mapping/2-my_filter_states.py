#!/usr/bin/python3
"""
Lists all states where name matches the
argument from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)
    cur = db.cursor()

    # Construct SQL query with format
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'
    ORDER BY id ASC".format(state_name)

    # Execute SQL query
    cur.execute(query)

    # Fetch all results and print them
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close database cursor and connection
    cur.close()
    db.close()
