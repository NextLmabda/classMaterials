import lib.data_preprocessing as dp
import pandas as pd

dummy_df = pd.DataFrame({'Name': ['Omolewa', 'David'], 'Salary': [1000, 2000], 'Country': ['USA', 'UK']})

def test_init():
    ts = dp.PreProcessing(dummy_df)

def test_get_categorical():
    ts = dp.PreProcessing(dummy_df)

    output1, output2 = ts.get_categorical()

    assert type(output1) == list
    assert type(output2) == list
    assert len(output1) == 0
    #TODO : Correct the get_categorical to handle numeric columns
    assert len(output2) == 3

def test_Encode_OHE():
    ts = dp.PreProcessing(dummy_df)
    _, output2 = ts.get_categorical()

    df = ts.OHE()

    assert (len(df.columns)) == 6