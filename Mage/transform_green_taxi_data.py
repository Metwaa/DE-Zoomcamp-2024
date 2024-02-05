import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    #print('passengers with zero data:', data['passenger_count'].isin([0]).sum())
    #print('trip_distance with zero data:', data['trip_distance'].isin([0]).sum())
    
    #to convert lpep_pickup_datetime from str to date
    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    #print(data['lpep_pickup_datetime'])
    
    # Create a new column to store pickup date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #to replace column space with underscore & lower all columns
    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.lower()
    )
    # filter the return value to be without 0 for passenger_count & trip_distance
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)];



@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are zero Passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are zero trip distance'