#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query cities and states, sort by city id
    cities = session.query(City).join(State).order_by(City.id).all()

    # print results
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
