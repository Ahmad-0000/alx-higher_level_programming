#!/usr/bin/python3
"""
This is a module that contains two classes. A "Base" class
and a "State" class that inherits from "Base" and then it's
mapped to a table in a database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
