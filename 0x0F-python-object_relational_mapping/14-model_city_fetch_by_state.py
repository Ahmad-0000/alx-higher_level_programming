#!/usr/bin/python3
"""
This is a script to fetch all the cities that alongside
with their states from two tables "cities" and "states".
username, password and database name must be provided as
command line arguments.
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    usr = argv[1]
    pawd = argv[2]
    db = argv[3]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pawd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.\
            query(State, City).order_by(City.id).\
            filter(State.id == City.state_id):
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
