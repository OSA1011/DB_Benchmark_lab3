import duckdb


size = "tiny"
def Q1_DuckDB():
    a = duckdb.sql(f"SELECT vendorid, count(*) FROM 'nyc_yellow_{size}.csv' GROUP BY 1").fetchall()

def Q2_DuckDB():
    a = duckdb.sql(f"SELECT passenger_count, avg(total_amount) FROM 'nyc_yellow_{size}.csv' GROUP BY passenger_count;").fetchall()

def Q3_DuckDB():
    a = duckdb.sql(f"SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM 'nyc_yellow_{size}.csv' GROUP BY 1, 2;").fetchall()

def Q4_DuckDB():
    a = duckdb.sql(f"SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM 'nyc_yellow_{size}.csv' GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;").fetchall()

