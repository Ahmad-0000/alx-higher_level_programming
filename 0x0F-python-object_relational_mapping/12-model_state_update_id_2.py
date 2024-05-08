#!/usr/bin/python3
"""
This is a script to update the "name" field in a row
with the "id" filed with the value 2 in a table mapped
to a the class "State".
username, password and database name must be supplied
as command line arguments
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, update
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    user = argv[1]
    pawd = argv[2]
    db = argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{pawd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = update(State).where(State.id).values(name="New Mexico")
    session.execute(stmt)
    session.commit()
    session.close()
