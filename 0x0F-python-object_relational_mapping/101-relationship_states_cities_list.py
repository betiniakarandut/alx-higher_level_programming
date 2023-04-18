#!/usr/bin/python3
""" Lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa """

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: ".format(state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
