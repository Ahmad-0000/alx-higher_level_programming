#!/usr/bin/python3
"""
This is a script to add a state to a table mapped to the
class "State" in a database.
username, password and the database name must be supplied
as command line arguments in this order.
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    usr = argv[1]
    pawd = argv[2]
    db = argv[3]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pawd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="Louisiana"))
    session.commit()
    session.close()
