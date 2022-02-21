import os
from datetime import datetime

import dateparser
import pandas as pd
from pandas import MultiIndex

from utils.duration import duration

idx = pd.IndexSlice


def roll_fund(df):
    return len(df)


def process_dates(start_date, end_date):
    ed = end_date
    if end_date is None:
        ed = dateparser.parse(str(datetime.date.today()))
    elif type(end_date) is str:
        ed = dateparser.parse(end_date)
    sd = start_date
    if type(start_date) is str:
        sd = dateparser.parse(start_date)
    return sd, ed


class TestMultiIndexDataframe:
    def setup_class(self):
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'source_data.csv'))
        df['time'] = pd.to_datetime(df['time'])
        df.set_index(['code', 'time'], inplace=True)
        self.source_data = df

    def test_batch_get_price(self):
        assert type(self.source_data.index) is MultiIndex
        assert len(self.source_data.index.levels) == 2
        assert self.source_data.index.names == ['code', 'time']

    def test_slice_df_by_security(self):
        slice_df = self.source_data.loc(axis=0)['000001.XSHE', :]
        print(slice_df)
        assert list(set(slice_df.index.get_level_values(0))) == ['000001.XSHE']

        slice_df2 = self.source_data.loc(axis=0)[idx['000001.XSHE', '000002.XSHE'], :]
        print(slice_df2)
        assert set(slice_df2.index.get_level_values(0)) == {'000001.XSHE', '000002.XSHE'}

        slice_xs_df = self.source_data.xs('000001.XSHE', level='code')
        print(slice_xs_df)

        slice_df_alt = self.source_data.loc[idx['000001.XSHE', :], :]
        print(slice_df_alt)

    def test_slice_df_by_date(self):
        sd, ed = process_dates('2022-01-05', '2022-01-15')
        slice_date_df = self.source_data.loc(axis=0)[idx[:, sd:ed]].copy()
        print(slice_date_df)
        date_index = list(sorted(set(slice_date_df.index.get_level_values(1))))
        print(date_index)
        assert date_index[0] >= sd and date_index[-1] <= ed

    def test_slice_df_by_codes_and_dates(self):
        sd, ed = process_dates('2022-01-05', '2022-01-15')
        slice_df = self.source_data.loc(axis=0)[idx[['000001.XSHE', '000002.XSHE'], sd:ed]]
        print(slice_df)
        assert set(slice_df.index.get_level_values(0)) == {'000001.XSHE', '000002.XSHE'}
        date_index = list(sorted(set(slice_df.index.get_level_values(1))))
        assert date_index[0] >= sd and date_index[-1] <= ed

    @duration
    def liquidity_if(self, source_data):
        source_data['liquidity'] = source_data.groupby('code')['money'].transform(lambda s: s.rolling(3).mean())
        source_data['liquidity_if'] = source_data['liquidity'] > 50000000

    def test_group_by_code_transform(self):
        self.liquidity_if(self.source_data)
        print(self.source_data)

    def test_group_by_nth(self):
        a = self.source_data.groupby('time').nth(5)
        print(a)
