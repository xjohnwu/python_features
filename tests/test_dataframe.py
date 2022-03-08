import pandas as pd
import pytest


def test_dataframe_head_tail():
    # initialize a dataframe
    df = pd.DataFrame(
        [[21, 72, 67],
         [23, 78, 62],
         [32, 74, 56],
         [73, 88, 67],
         [32, 74, 56],
         [43, 78, 69],
         [32, 74, 54],
         [52, 54, 76]],
        columns=['a', 'b', 'c'])

    # get first 3 rows
    df1 = df.head(3)

    # print the dataframe
    print(df1)
    assert 3 == len(df1)

    df2 = df.tail(4)
    print(df2)
    assert 4 == len(df2)

    for index, series in df.head(3).iterrows():
        print(series['a'])


def test_dataframe_empty_df():
    df = pd.DataFrame()
    with pytest.raises(KeyError):
        print(df['BTCUSDT'])
