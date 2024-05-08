#!/usr/bin/python3
"""
This is a script to print the states that contain
the the letter "a".
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    usr = argv[1]
    pawd = argv[2]
    db = argv[3]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pawd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = "name LIKE BINARY '%a%'"
    for state in session.query(State).order_by(State.id).filter(text(stmt)):
        print(f"{state.id}: {state.name}")
