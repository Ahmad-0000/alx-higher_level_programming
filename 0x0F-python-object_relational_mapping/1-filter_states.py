#!/usr/bin/python3
"""
This is a script to list rows that has the attribute
"name" values starting with "N" from a "states" table.
The database username, password and name must be supplied
as command line arguments
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    u = argv[1]
    p = argv[2]
    db = argv[3]
    con = MySQLdb.connect(user=u, passwd=p, db=db, host="localhost", port=3306)
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
