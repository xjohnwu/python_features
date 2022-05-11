import pandas as pd
import os


def test_read_excel():
    excel = os.path.join(os.path.dirname(__file__), "position.xlsx")

    df = pd.read_excel(excel, convert_float=False, index_col=0)
    print(df)


def test_split():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'address_data.csv'), index_col=0)
    df['state'] = df['place_with_parent_names'].str.split('|', expand=True)[2]
    print(df)
