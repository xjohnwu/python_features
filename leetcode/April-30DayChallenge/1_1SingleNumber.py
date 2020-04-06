"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List

import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


@pytest.mark.parametrize("test_input,expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.singleNumber(test_input) == expected
