#!/usr/bin/python3
"""Defines the City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Represents a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        id (int): unique id generated automatically, cannot be null,
            primary key
        name (str): name of the city, cannot be null
        state_id (int): id of the state that the city is in, cannot be null,
            foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
