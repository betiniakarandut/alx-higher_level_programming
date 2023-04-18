#!/usr/bin/python3
"""Defines the State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        id (int): unique id generated automatically, cannot be null,
            primary key
        name (str): name of the state, cannot be null
        cities (relationship): represents a relationship with the City class.
            If a State object is deleted, all linked City objects will be
            automatically deleted.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
