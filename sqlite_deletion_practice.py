#goal: delete a row from a table in the cats database
import sqlite3

def delete_cat(conn, id):
    """
    delete a specified row from the cats table
    :param conn: connection object
    :param id: primary key id for row
    :return:
    """
    sql = "DELETE FROM cats WHERE id = ?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    
def delete_kitten(conn, id):
    """
    delete a specified row from the kittens table
    :param conn: connection object
    :param id: primary key id for row
    :return:
    """
    sql = "DELETE FROM kittens WHERE id = ?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    
def delete_all_cats(conn):
    """
    delete all rows from cats table
    :param conn: connection object
    :return:
    """
    sql = "DELETE FROM cats"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
def delete_all_kittens(conn):
    """
    delete all rows from kittens table
    :param conn: connecton object
    :return:
    """
    sql = "DELETE FROM kittens"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
def main():
    db_file = r"c:\sqlite\db\cats.db"
    conn = sqlite3.connect(db_file)
    with conn:
        delete_kitten(conn,2)
        
if __name__ == "__main__":
    main()