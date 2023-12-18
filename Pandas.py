import pandas as pd
import time
pd.options.mode.chained_assignment = None
trips = pd.read_csv("nyc_yellow_tiny.csv")

def Q1_Pandas():
    selected_df = trips[['VendorID']]
    grouped_df = selected_df.groupby('VendorID')
    final_df = grouped_df.size().reset_index(name='counts')
    #print(final_df)

def Q2_Pandas():
    selected_df = trips[['passenger_count', 'total_amount']]
    grouped_df = selected_df.groupby('passenger_count')
    final_df = grouped_df.mean().reset_index()
    #print(final_df)

def Q3_Pandas():
    selected_df = trips[['passenger_count', 'tpep_pickup_datetime']]
    selected_df['year'] = pd.to_datetime(
        selected_df.pop('tpep_pickup_datetime'),
        format='%Y-%m-%d %H:%M:%S').dt.year
    grouped_df = selected_df.groupby(['passenger_count', 'year'])
    final_df = grouped_df.size().reset_index(name='counts')
    #print(final_df)

def Q4_Pandas():
    selected_df = trips[[
        'passenger_count',
        'tpep_pickup_datetime',
        'trip_distance']]
    selected_df['trip_distance'] = selected_df['trip_distance'].round().astype(int)
    selected_df['year'] = pd.to_datetime(
        selected_df.pop('tpep_pickup_datetime'),
        format='%Y-%m-%d %H:%M:%S').dt.year
    grouped_df = selected_df.groupby([
        'passenger_count',
        'year',
        'trip_distance'])
    final_df = grouped_df.size().reset_index(name='counts')
    final_df = final_df.sort_values(
        ['year', 'counts'],
        ascending=[True, False])
    #print(final_df)



