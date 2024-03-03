import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'
    
    taxi_dtypes = {
                    'VendorID' : pd.Int64Dtype(),
                    'passanger_count' : pd.Int64Dtype(),
                    'Trip_distance' : float,
                    'RateCodeID' : pd.Int64Dtype(),
                    'Store_and_fwd_flag' : str,
                    'PULocationID' : pd.Int64Dtype(),
                    'DOLocationID' : pd.Int64Dtype(),
                    'Payment_type' : pd.Int64Dtype(),
                    'Fare_amount' : float,
                    'Extra' : float,
                    'MTA_tax' : float,
                    'Tip_amount' : float,
                    'Tolls_amount' : float,
                    'Improvement_surcharge' : float,
                    'Total_amount' : float,
                    'Congestion_Surcharge' : float
                }

    parse_dates = ['tpep_pickup_datetime' , 'tpep_dropoff_datetime']
    
    return pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
