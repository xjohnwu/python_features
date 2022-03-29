from retry import retry

i = 0


@retry(tries=3)
def run_3_times():
    global i
    i += 1
    raise Exception("I want to retry again!")


def test_retry():
    try:
        run_3_times()
    except:
        print('Expected')
    global i
    assert i == 3
