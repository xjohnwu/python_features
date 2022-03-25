from queue import Queue


def test_Queue():
    queue = Queue()
    queue.put(10)
    queue.put(11)
    assert queue.qsize() == 2
    assert 10 == queue.get()
    assert 11 == queue.get()
    assert queue.qsize() == 0
