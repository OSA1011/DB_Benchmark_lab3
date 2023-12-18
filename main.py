from Pandas import *
from DuckDB import *
from sqlite import *
from psycopg import *
from SQLAlchemy import *
import time
from statistics import median


def work_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

# def tt():
#     connection = sqlite3.connect('DB_Browser.db')
#     cursor = connection.cursor()
#     query = "SELECT vendorid, count(*) FROM nyc_yellow_tiny GROUP BY 1;"
#     cursor.execute(query)
#     # records = cursor.fetchall()
#     connection.commit()
#     connection.close()

arr = [[Q1_Psycopg, Q2_Psycopg, Q3_Psycopg, Q4_Psycopg], [Q1_SQLite, Q2_SQLite, Q3_SQLite, Q4_SQLite],
        [Q1_DuckDB, Q2_DuckDB, Q3_DuckDB, Q4_DuckDB], [Q1_Pandas, Q2_Pandas, Q3_Pandas, Q4_Pandas]]
for lib in arr:
    for func in lib:
        print(work_time(func), end='   ')
    print('\n')
#print(work_time(tt))