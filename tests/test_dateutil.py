from datetime import timedelta, datetime
from dateutil import tz
from dateutil.parser import isoparse


def test_isoparse():
    dt = isoparse('2020-06-13T22:54:57.404Z')
    print(dt)
    assert dt == datetime(2020, 6, 13, 22, 54, 57, 404000, tzinfo=tz.UTC)
    assert dt.utcoffset() == timedelta(0)
