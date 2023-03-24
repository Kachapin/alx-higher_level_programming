#!/usr/bin/python3
""" State class definition file
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, relationship
from sqlalchemy import create_engine


Base = declarative_base()


class State(Base):
    """ State class representation """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")
