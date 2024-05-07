#!/usr/bin/python3
"""
A script to list all the cities of a particular state.
Useraname, password, database name and the state name must
be provided as a command line arguemnts in the same order.
This script is SQL injection safe.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    u = argv[1]
    p = argv[2]
    d = argv[3]
    s = argv[4]
    con = MySQLdb.connect(user=u, passwd=p, db=d, port=3306, charset="utf8")
    cur = con.cursor()
    cur.execute("""SELECT c.name FROM
            cities c INNER JOIN states s
            ON s.id = c.state_id
            WHERE s.name = %(s)s""", {'s': s})
    cities = cur.fetchall()
    if cities:
        i = len(cities)
        for _ in range(i):
            if _ == i - 1:
                print(f"{cities[_][0]}")
            else:
                print(f"{cities[_][0]}, ", end="")
    else:
        print()
