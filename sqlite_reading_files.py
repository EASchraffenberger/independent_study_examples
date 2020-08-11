#Goal: create a database and populate it with data read from a local .csv file.

#practice: reading multiple .csv file into a dictionary object, creating a database with the resulting tables, and printing the tables to the screen.
import csv
import sqlite3

def drop_table(conn, table_name):
    """
    Drops table from parameter statement
    :param conn: connection object
    :param drop_table_sql: sql DROP TABLE segment
    """
    sql = """DROP TABLE {};""".format(table_name)
    c = conn.cursor()
    c.execute(sql)

def create_table(conn, create_table_sql):
    """
    Creates table from parameter statement
    :param conn: connection object
    :param create_table_sql: sql CREATE TABLE statement
    """
    c = conn.cursor()
    c.execute(create_table_sql)
    
def read_csv(filepath):
    """
    Reads vsc file and returns content as a list of strings.
    :param filepath: path and name of file, in quotes
    :return: list of strings (one row = one string)
    """
    csvfile = open(filepath, newline = '')
    reader = csv.reader(csvfile, delimiter = ',')
    return reader

def insert_row(conn, table_name, column_names, row):
    #don't forget to re-add "conn" and "row" parameter after testing!
    """inserts one string from csv file into table to create new row
    :param conn: connection object
    :param table_name: name of table
    :param column_names: string of column names, delineated with commas
    :param row: string from csv file"""
    #generate a string of question marks to be inserted into VALUES():
    number_of_columns = len(column_names.split())
    variable_string = ""
    x = 0
    while x < number_of_columns:
        if x == number_of_columns -1:
            variable_string = variable_string + "?"
        else:
            variable_string = variable_string + "?, "
        x = x + 1
    sql = """INSERT OR REPLACE INTO {0}({1}) VALUES({2})""".format(table_name, column_names, variable_string)
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()

def display_table(conn, table_name):
    print('This is the {} table:'.format(table_name))
    sql = """SELECT * FROM {}""".format(table_name)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    db_file = r"C:\sqlite\db\company_example.db"
    with sqlite3.connect(db_file) as conn:
        #drop tables:
        drop_table(conn, 'EMPLOYEES')
        drop_table(conn, 'JOB_HISTORY')
        drop_table(conn, 'JOBS')
        drop_table(conn, 'DEPARTMENTS')
        drop_table(conn, 'LOCATIONS')

        #creating tables in database:
        sql_create_employees = """CREATE TABLE IF NOT EXISTS EMPLOYEES(
                                EMP_ID CHAR(9) NOT NULL, 
                                F_NAME VARCHAR(15) NOT NULL,
                                L_NAME VARCHAR(15) NOT NULL,
                                SSN CHAR(9),
                                B_DATE DATE,
                                SEX CHAR,
                                ADDRESS VARCHAR(30),
                                JOB_ID CHAR(9),
                                SALARY DECIMAL(10,2),
                                MANAGER_ID CHAR(9),
                                DEP_ID CHAR(9) NOT NULL,
                                PRIMARY KEY (EMP_ID));"""

        sql_create_job_history = """CREATE TABLE IF NOT EXISTS JOB_HISTORY (
                                EMPL_ID CHAR(9) NOT NULL, 
                                START_DATE DATE,
                                JOBS_ID CHAR(9) NOT NULL,
                                DEPT_ID CHAR(9),
                                PRIMARY KEY (EMPL_ID,JOBS_ID));"""

        sql_create_jobs = """CREATE TABLE IF NOT EXISTS JOBS(
                        JOB_IDENT CHAR(9) NOT NULL, 
                        JOB_TITLE VARCHAR(15) ,
                        MIN_SALARY DECIMAL(10,2),
                        MAX_SALARY DECIMAL(10,2),
                        PRIMARY KEY (JOB_IDENT));"""

        sql_create_departments = """CREATE TABLE IF NOT EXISTS DEPARTMENTS(
                                DEPT_ID CHAR(9) NOT NULL, 
                                DEP_NAME VARCHAR(15) ,
                                MANAGER_ID CHAR(9),
                                LOC_ID CHAR(9),
                                PRIMARY KEY (DEPT_ID));"""

        sql_create_locations = """CREATE TABLE IF NOT EXISTS LOCATIONS(
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));"""

        create_table(conn, sql_create_employees)
        create_table(conn, sql_create_job_history)
        create_table(conn, sql_create_jobs)
        create_table(conn, sql_create_departments)
        create_table(conn, sql_create_locations)

        #adding rows to tables:
        employee_reader = read_csv(r'C:\Users\lizsc\Downloads\Employees.csv')
        job_history_reader = read_csv(r'C:\Users\lizsc\Downloads\JobsHistory.csv')
        job_reader = read_csv(r'C:\Users\lizsc\Downloads\Jobs.csv')
        department_reader = read_csv(r'C:\Users\lizsc\Downloads\Departments.csv')
        location_reader = read_csv(r'C:\Users\lizsc\Downloads\Locations.csv')

        for row in employee_reader:
            insert_row(conn, 'EMPLOYEES', 'EMP_ID, F_NAME, L_NAME, SSN, B_DATE, SEX, ADDRESS, JOB_ID, SALARY, MANAGER_ID, DEP_ID', row)

        for row in job_history_reader:
            insert_row(conn, 'JOB_HISTORY', 'EMPL_ID, START_DATE, JOBS_ID, DEPT_ID', row)

        for row in job_reader:
            insert_row(conn, 'JOBS', 'JOB_IDENT, JOB_TITLE, MIN_SALARY, MAX_SALARY', row)

        for row in department_reader:
            insert_row(conn, 'DEPARTMENTS', 'DEPT_ID, DEP_NAME, MANAGER_ID, LOC_ID', row)

        for row in location_reader:
            insert_row(conn, 'LOCATIONS', 'LOCT_ID, DEP_ID_LOC', row)

        #Displaying tables:
        display_table(conn, 'EMPLOYEES')
        display_table(conn, 'JOB_HISTORY')
        display_table(conn, 'JOBS')
        display_table(conn, 'JOB_HISTORY')
        display_table(conn, 'DEPARTMENTS')
        display_table(conn, 'LOCATIONS')

#running main program
if __name__ == "__main__":
    main()        