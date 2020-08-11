import sqlite3
from sqlite3 import Error
#goal: update an existing row

def update_cat(conn, cats):
    """
    update a row from the cat table
    :param conn: connection object
    :param cat: cat table
    :return: row id
    """
    sql = """UPDATE cats
          SET name = ?,
            age = ?
            snuzziness = ?
          WHERE id =?"""
    cur = conn.cursor()
    cur.execute(sql, cats)
    conn.commit()
    return cur.lastrowid
    
def update_kitten(conn, kittens):
    """
    update a row from the kitten table
    :param conn: connection object
    :param kitten: kitten table
    :return: row id
    """
    sql = """UPDATE kittens
          SET name = ?,
            age = ?,
            cuteness = ?,
            housetrained = ?
          WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, kittens)
    conn.commit()
    return cur.lastrowid
    
def main():
    db_file = r"C:\sqlite\db\cats.db"
    conn = sqlite3.connect(db_file)
    
    with conn:
        update_kitten(conn, ("Shiny New Kitten", 1, 7, 0, 2))
  
if __name__ == "__main__":
    main()
    