"""
202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
import pytest


class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        single_numbers = set()
        while True:
            dec = 1
            square_sum = 0
            while dec <= num:
                dec *= 10
                square_sum += pow(int((num % dec) / (dec / 10)), 2)
            if dec == 10:
                if square_sum == 1:
                    return True
                elif square_sum not in single_numbers:
                    single_numbers.add(square_sum)
                else:
                    return False
            num = square_sum
            print(num)

    def isHappy_slow(self, n: int) -> bool:
        num = n
        single_numbers = set()
        while True:
            splits = [int(s) for s in str(num)]
            if len(splits) == 1:
                single_number = splits[0]
                if single_number == 1:
                    return True
                elif single_number not in single_numbers:
                    single_numbers.add(single_number)
                else:
                    return False
            num = sum([pow(i, 2) for i in splits])


@pytest.mark.parametrize("test_input,expected", [(19, True), (1, True), (7, True), (200, False)])
def test_solution(test_input, expected):
    s = Solution()
    assert s.isHappy(test_input) == expected
