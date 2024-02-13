import io
import pandas as pd
import requests
import pyarrow as pa
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{}.parquet'
    
    # used in loop for range less than 10
    x=''
    df_list = []
#Using for loop to read parquet green taxi for year 2022     
    for i in range(1, 13):
        
        # to add 0 before 1:9 to catch the right url
        if i < 10:
            x = "0" + str(i)
            df_list.append(pd.read_parquet(url.format(x),  engine='pyarrow'))
            df = pd.concat(df_list)
        else:
            df_list.append(pd.read_parquet(url.format(i), engine='pyarrow'))
            df = pd.concat(df_list)

    return (df)