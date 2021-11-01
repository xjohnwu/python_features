# 输入一个1-N排列P, 求一个区间[a, b], pos[x] 为x在P中的位置 使得pos[a] <= pos[a..b] <= pos[b], 且b-a最大
# 1 3 4 5 2 => 3 5
# 1 4 3 5 2 => 1 2 or 4 5
# 2 1 3 5 4 => 2 4
import pytest


class Sequence:
    def __init__(self, first):
        self.first = first
        self.last = first
        self.num = 1

    def test(self, next_el):
        return next_el == self.last + 1

    def update(self, last):
        assert last == self.last + 1
        self.last = last
        self.num += 1


def idiot(p: list):
    sequences = [Sequence(p[0])]
    for i in range(1, len(p)):
        for seq in list(sequences):
            if seq.test(p[i]):
                seq.update(p[i])
            elif p[i] > seq.last:
                sequences.append(Sequence(p[i]))
            elif p[i] < seq.last:
                continue
            else:
                raise ValueError(p[i])
    max_seq = sequences[0]
    for seq in sequences[1:]:
        if seq.num > max_seq.num:
            max_seq = seq

    return max_seq.first, max_seq.last


@pytest.mark.parametrize("test_input,expected", [
    ([1, 3, 4, 5, 2], (3, 5)),
    ([1, 4, 3, 5, 2], (1, 2)),
    ([2, 1, 3, 5, 4], (2, 4)),
])
def test_problems(test_input, expected):
    assert expected == idiot(test_input)
