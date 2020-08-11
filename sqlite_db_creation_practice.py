import sqlite3
from sqlite3 import Error

#Goal: create Sqlite database from scratch
    
def create_table(conn, create_table_sql):
    """
    create_table creates a table
    :param conn: the Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)

        
#the main() function is where the database tables are created:
def main():
    database = r"C:\sqlite\db\cats.db"
    
    sql_create_cats_table = """CREATE TABLE IF NOT EXISTS cats(
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                age integer,
                                snuzziness float
                                );"""
                                
    sql_create_kittens_table = """CREATE TABLE IF NOT EXISTS kittens(
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    age integer,
                                    cuteness float,
                                    housetrained integer
                                    );"""                               
    #create a database connection:
    conn = sqlite3.connect(database)
    if conn is not None:
        #create cats table:
        create_table(conn, sql_create_cats_table)                     
        #create kittens table:
        create_table(conn, sql_create_kittens_table)
    else:
        print("Could not create database connection. Do better n00b.")
      
#execute main function:
if __name__ == '__main__':
    main()
                           
                                