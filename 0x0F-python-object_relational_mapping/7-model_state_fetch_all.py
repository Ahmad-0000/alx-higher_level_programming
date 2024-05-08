#!/usr/bin/python3
"""
This is a script to print the states objects
from a database table.
The username, password and database name must
be provided as command line arguments in the
preceeded order.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

usr = argv[1]
pawd = argv[2]
db = argv[3]

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{usr}:{pawd}@localhost:3306/{db}")

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
    session.close()
