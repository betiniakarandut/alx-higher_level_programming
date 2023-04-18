#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':
    # script should take 3 arguments: mysql username, mysql password and database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # retrieve all City objects and their linked State object
    cities = session.query(City).order_by(City.id).all()

    # print the desired output
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
