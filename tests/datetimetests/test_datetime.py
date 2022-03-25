import time
from datetime import date, datetime, timedelta

from dateutil.parser import isoparse
from dateutil import tz


def test_datetime():
    print(datetime.min)
    print(datetime.utcnow())
    assert datetime.min < datetime.utcnow()


def test_timespan():
    now = datetime.utcnow()
    time.sleep(1)
    print(datetime.utcnow() - now)
    assert datetime.utcnow() - now >= timedelta(seconds=1)


def test_date():
    print("Today(datetime):", str(datetime.today()))
    print("Today(date):", str(date.today()))
    print("UTC today:", str(datetime.utcnow().date()))


def test_isoparse():
    dt = isoparse('2020-06-13T22:54:57.404Z')
    print(dt)
    assert dt == datetime(2020, 6, 13, 22, 54, 57, 404000, tzinfo=tz.UTC)
    assert dt.utcoffset() == timedelta(0)
