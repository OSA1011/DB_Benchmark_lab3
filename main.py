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


arr = [[Q1_Psycopg, Q2_Psycopg, Q3_Psycopg, Q4_Psycopg], [Q1_SQLite, Q2_SQLite, Q3_SQLite, Q4_SQLite],
        [Q1_DuckDB, Q2_DuckDB, Q3_DuckDB, Q4_DuckDB], [Q1_Pandas, Q2_Pandas, Q3_Pandas, Q4_Pandas]]
for lib in arr:
    for func in lib:
        a = []
        for i in range(11):
            a.append(work_time(func))
        print(median(a), end='   ')
    print('\n')