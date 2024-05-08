#!/usr/bin/python3
"""
This is a script to delete the rows with a "name" field
value containing the letter "a" in a table mapped to the
class "State" in a database.
username, password and database name must be supplied as
command line arguments in the same order.
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker

    usr = argv[1]
    pawd = argv[2]
    db = argv[3]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pawd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.execute(text("DELETE FROM states WHERE name LIKE BINARY '%a%'"))
    session.commit()
    session.close()
