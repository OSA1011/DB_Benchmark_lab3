import sqlite3
import csv


size = "tiny"
def Q1_SQLite():
    connection = sqlite3.connect('nyc_yellow_tiny.db')
    cursor = connection.cursor()
    query = f"SELECT vendorid, count(*) FROM nyc_yellow_{size} GROUP BY 1;"
    cursor.execute(query)
    connection.commit()
    connection.close()

def Q2_SQLite():
    connection = sqlite3.connect('nyc_yellow_tiny.db')
    cursor = connection.cursor()
    query = f"SELECT passenger_count, avg(total_amount) FROM nyc_yellow_{size} GROUP BY 1;"
    cursor.execute(query)
    connection.commit()
    connection.close()

def Q3_SQLite():
    connection = sqlite3.connect('nyc_yellow_tiny.db')
    cursor = connection.cursor()
    query = f"SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM nyc_yellow_{size} GROUP BY 1, 2;"
    cursor.execute(query)
    connection.commit()
    connection.close()

def Q4_SQLite():
    connection = sqlite3.connect('nyc_yellow_tiny.db')
    cursor = connection.cursor()
    query = f"SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM nyc_yellow_{size} GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;"
    cursor.execute(query)
    connection.commit()
    connection.close()



# Устанавливаем соединение с базой данных
def connect():
    connection = sqlite3.connect('nyc_yellow_tiny.db')
    cursor = connection.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS nyc_yellow_{size} (
                                            
                                            VendorID int,
                                            tpep_pickup_datetime      datetime,
                                            tpep_dropoff_datetime     datetime,
                                            passenger_count          float,
                                            trip_distance            float,
                                            RatecodeID               float,
                                            store_and_fwd_flag        varchar(1),
                                            PULocationID               int,
                                            DOLocationID               int,
                                            payment_type               int,
                                            fare_amount              float,
                                            extra                    float,
                                            mta_tax                  float,
                                            tip_amount               float,
                                            tolls_amount             float,
                                            improvement_surcharge    float,
                                            total_amount             float, 
                                            congestion_surcharge     float,
                                            airport_fee              float,
                                            Airport_fee2              float
    )
    ''')

    #file = open('C:\\Users\\Arnau\\PycharmProjects\\DB_lab3\\nyc_yellow_tiny.csv', "r")
    #content = csv.reader(file)
    with open(f'C:\\Users\\Arnau\\PycharmProjects\\DB_lab3\\nyc_yellow_{size}.csv', "r") as table:
        dr = csv.DictReader(table)
        to_db = [( i['VendorID'], i['tpep_pickup_datetime'], i['tpep_dropoff_datetime'], i['passenger_count'], i['trip_distance'], i['RatecodeID'],
                  i['store_and_fwd_flag'], i['PULocationID'], i['DOLocationID'], i['payment_type'], i['fare_amount'], i['extra'], i['mta_tax'], i['tip_amount'],
                  i['tolls_amount'], i['improvement_surcharge'], i['total_amount'], i['congestion_surcharge'], i['airport_fee'], i['Airport_fee']) for i in dr]
    cursor.executemany(f'INSERT INTO nyc_yellow_{size} VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', to_db)
    #a = cursor.execute("SELECT * FROM nyc_yellow_tiny").fetchall()
    connection.commit()
    connection.close()
    #Q4_SQLite()
    #(i['\"Unnamed: 0\"'],