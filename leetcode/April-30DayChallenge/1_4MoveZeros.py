"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List

import pytest


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                for i in range(index + 1, len(nums)):
                    if nums[i] != 0:
                        nums[index] = nums[i]
                        nums[i] = 0
                        break
            index += 1


@pytest.mark.parametrize("test_input,expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1]),
    ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0])
])
def test_solution(test_input, expected):
    s = Solution()
    s.moveZeroes(test_input)
    assert test_input == expected
