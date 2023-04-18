#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create connection
    db_user = sys.argv[1]
    db_pwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(db_user, db_pwd, db_name),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and print them
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
