"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
import sys
from typing import List

import pytest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = None
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            res = max(res, cur_sum) if res is not None else cur_sum
        return res


@pytest.mark.parametrize("test_input,expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.maxSubArray(test_input) == expected
