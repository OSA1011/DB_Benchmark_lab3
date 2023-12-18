import psycopg2


size = "big"
def Q1_Psycopg():
    with connection.cursor() as cursor:
        q1 = f"SELECT vendorid, count(*) FROM nyc_yellow_{size} GROUP BY 1;"
        cursor.execute(q1)
        records = cursor.fetchall()
        connection.commit()
        #print(records)


def Q2_Psycopg():
    with connection.cursor() as cursor:
        query = f"SELECT passenger_count, avg(total_amount) FROM nyc_yellow_{size} GROUP BY 1;"
        cursor.execute(query)
        records = cursor.fetchall()
        connection.commit()
        #print(records)

def Q3_Psycopg():
    with connection.cursor() as cursor:
        query = f"SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM nyc_yellow_{size} GROUP BY 1, 2;"
        cursor.execute(query)
        records = cursor.fetchall()
        connection.commit()
        #print(records)

def Q4_Psycopg():
    with connection.cursor() as cursor:
        query = f"SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM nyc_yellow_{size} GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;"
        cursor.execute(query)
        records = cursor.fetchall()
        connection.commit()
        #print(records)

connection = psycopg2.connect( database='postgres',
                               user='postgres',
                               password='Arnautov3011',
                               host='localhost')

def connecting():
    with connection.cursor() as cursor:
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS nyc_yellow_{size} 
                                        (\"Unnamed: 0\" int,
                                        VendorID int,
                                        tpep_pickup_datetime      timestamp,
                                        tpep_dropoff_datetime     timestamp,
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
                                        Airport_fee2              float);""")

        csvf = open(f"C:\\Users\\Arnau\\PycharmProjects\\DB_lab3\\nyc_yellow_{size}.csv", "r")
        cursor.copy_expert(f'''COPY nyc_yellow_{size}  
                              FROM STDIN 
                              DELIMITER ',' 
                              CSV HEADER;''', csvf)
        connection.commit()
        #connection.close()
connecting()
