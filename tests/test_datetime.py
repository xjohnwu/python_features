import time
from datetime import datetime, timedelta


def test_datetime():
    print(datetime.min)
    print(datetime.utcnow())
    assert datetime.min < datetime.utcnow()


def test_timespan():
    now = datetime.utcnow()
    time.sleep(1)
    print(datetime.utcnow() - now)
    assert datetime.utcnow() - now >= timedelta(seconds=1)
