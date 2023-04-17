import sys
import MySQLdb

# Connect to the database using command line arguments
db = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    port=3306
)

# Create a cursor object
cursor = db.cursor()

# Execute the query to select all states, sorted by id
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows and print them
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
db.close()

