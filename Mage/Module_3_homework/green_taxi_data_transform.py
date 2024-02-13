import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    #to convert lpep_pickup_datetime from str to date
    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'],format='%d-%m-%y')

    # Create a new column to store pickup date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.strftime('%d/%m/%y')

    return data