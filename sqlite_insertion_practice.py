#goal: insert rows into cat and kitten tables created in sqlite_practice2.py
import sqlite3
from sqlite3 import Error

def create_cat(conn, cats):
    """
    create_cat inserts a new row into the cats table.
    :param conn: connection object
    :param cats: cats table
    :return: row id
    """
    sql = """INSERT INTO cats(name, age, snuzziness) VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, cats)
    conn.commit()
    return cur.lastrowid

def create_kitten(conn, kittens):
    """
    create_kitten inserts a new row into the kittens table.
    :param conn: connection object
    :param kittens: kittens table
    :return: row id
    """
    sql = """INSERT INTO kittens(name, age, cuteness, housetrained) VALUES(?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, kittens)
    conn.commit()
    return cur.lastrowid
    
def main():
    database = r"C:\sqlite\db\cats.db"
    #create a database connection
    conn = sqlite3.connect(database)
 
    if conn is not None:
        with conn:
            #insert rows into cats table:
            cat1 = ("Magma", 8, 10)
            cat1_id = create_cat(conn, cat1)
            cat2 = ("KittyCow", 6, 5)
            cat2_id = create_cat(conn, cat2)
            #insert rows into kittens table:
            kitten1 = ("Princess NoFace", 1, 2, 1)
            kitten1_id = create_kitten(conn, kitten1)
            kitten2 = ("Jasper", 1, 6, 0)
            kitten2_id = create_kitten(conn, kitten2)
    else:
        print("Could not create database connection. Get good, n00b.")
       
#run main():
if __name__ == '__main__':
    main()
        