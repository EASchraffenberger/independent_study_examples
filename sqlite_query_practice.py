import sqlite3
#goal: execute SELECT statements

def select_all_cats(conn):
    """
    Selects and displays all rows from cats table
    :param conn: connection object
    :return:
    """
    sql = "SELECT * FROM cats"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
def select_all_kittens(conn):
    """
    Selects and displays all rows from the cats table
    :param conn: connection object
    :return:
    """
    sql = "SELECT * FROM kittens"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
def select_cats_by_name(conn, name)
    """
    