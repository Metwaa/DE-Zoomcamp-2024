import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{}.csv.gz'

    taxi_dtypes = {
                    'VendorID' : pd.Int64Dtype(),
                    #'lpep_pickup_datetime' : pd.datetime('lpep_pickup_datetime'),
                    #'lpep_dropoff_datetime' : pd.datetime('lpep_dropoff_datetime'),
                    'store_and_fwd_flag' : str, 
                    'RateCodeID' : pd.Int64Dtype(),
                    'PULocationID' : pd.Int64Dtype(),
                    'DOLocationID' : pd.Int64Dtype(),
                    'passenger_count' : pd.Int64Dtype(),
                    'trip_distance' : float,
                    'fare_amount' :  float,
                    'extra' :  float,
                    'mta_tax' : float,
                    'tip_amount' : float,
                    'tolls_amount' : float,
                    'ehail_fee' : str,
                    'improvement_surcharge' :  float,
                    'total_amount' : float,
                    'payment_type' : pd.Int64Dtype(),
                    'trip_type' : pd.Int64Dtype(),
                    'Congestion_Surcharge' : float
                }

#Using for loop to read data for the final quarter of 2020
    df_list = []
    for i in range(10, 13):
        #print('the url ', i ,' is:', url.format(i))
        df_list.append(pd.read_csv(url.format(i), sep=',', compression='gzip', dtype=taxi_dtypes))
        df = pd.concat(df_list)

    return (df)