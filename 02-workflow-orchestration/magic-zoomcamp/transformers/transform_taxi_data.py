import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Remove rows where passenger count is 0 and trip distance is 0
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    
    # Convert lpep_pickup_datetime to date and create lpep_pickup_date column
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.strftime('%Y-%m-%d')
    
    # Rename columns from Camel Case to Snake Case
    column_mapping = {
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }

    data.rename(columns=column_mapping, inplace=True)
    return data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['vendor_id'].isin(output['vendor_id']).all(), "vendor_id is not one of the existing values in the column."
    assert (output['passenger_count'] > 0).all(), "passenger_count is not greater than 0."
    assert (output['trip_distance'] > 0).all(), "trip_distance is not greater than 0."
    