#!/usr/bin/python3
"""
This is a script to print the "id" of a given state.
username, password, database name and the state name
must be supplied as command line arguments in the
preceeded order.
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    u = argv[1]
    p = argv[2]
    d = argv[3]
    s = argv[4]

    engine = create_engine(f"mysql+mysqldb://{u}:{p}@localhost:3306/{d}")
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).order_by(State.id).filter(State.name == s).all()
    if res:
        print(res[0].id)
    else:
        print("Not found")
    session.close()
