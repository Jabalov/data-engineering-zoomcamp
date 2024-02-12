import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': 'float64',  
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': 'str', 
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': 'float64', 
        'extra': 'float64',  
        'mta_tax': 'float64', 
        'trip_amount': 'float64', 
        'tolls_amount': 'float64', 
        'improvement_surcharge': 'float64', 
        'total_amount': 'float64',  
        'congestion_surcharge': 'float64',  
    }

    green_taxi_data = pd.DataFrame()

    for month_ in ['10', '11', '12']:
        link = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month_}.csv.gz'

        df = pd.read_csv(link, sep=",", compression='gzip', dtype=taxi_dtypes)
        green_taxi_data = pd.concat([green_taxi_data, df])
        
    return green_taxi_data
 


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
