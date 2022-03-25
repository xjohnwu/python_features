from collections import deque


def test_deque():
    queue = deque("abcde")
    assert "e" == queue.pop()
    assert "a" == queue.popleft()
