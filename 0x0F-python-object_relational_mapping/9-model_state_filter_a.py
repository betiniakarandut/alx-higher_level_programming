#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Initializes engine for connection to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(mysql_username, mysql_password, database_name))

    # Creates all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # Creates a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Querying the database for all states containing letter a
    contd = filter(State.name.like('%a%')).order_by(State.id).all()
    states = session.query(State).contd

    # Printing the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
