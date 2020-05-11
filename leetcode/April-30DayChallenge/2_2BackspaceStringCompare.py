"""
Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

from collections import deque

import pytest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.process(S) == self.process(T)

    @staticmethod
    def process(str_arr: str):
        q = deque()
        for c in str_arr:
            if c == '#':
                if len(q) > 0:
                    q.pop()
            else:
                q.append(c)
        return q


@pytest.mark.parametrize("S,T,expected", [
    ("ab#c", "ad#c", True),
    ("ab##", "ad##", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False),
])
def test_solution(S, T, expected):
    s = Solution()
    assert s.backspaceCompare(S, T) == expected
