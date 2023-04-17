#!/usr/bin/python3
# Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
import sys
import MySQLdb

def main():
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT * FROM `states` WHERE `name` LIKE BINARY '{}' ORDER BY `id`".format(sys.argv[4])
    c.execute(query)
    [print(state) for state in c.fetchall()]
    db.close()

if __name__ == "__main__":
    main()

