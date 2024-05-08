#!/usr/bin/python3
"""
This is a script that contain a class "City" to be mapped
to the table "cities" in a particular database
"""
from model_state import Base
from sqlalchemy import Integer, Column, String, ForeignKey


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
