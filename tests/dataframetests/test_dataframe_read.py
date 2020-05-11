import pandas as pd
import os


def test_read_excel():
    excel = os.path.join(os.path.dirname(__file__), "position.xlsx")

    df = pd.read_excel(excel, convert_float=False, index_col=0)
    print(df)
