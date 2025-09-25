#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

import numpy as np


# This is what the Python team would write:
LEETCODE_COMMON_BOUNDS = {
    "small": (-100, 100),
    "medium": (-(10**4), 10**4),
    "large": (-(10**9), 10**9),
    "huge": (-(2**31), 2**31 - 1),
}

# Simple, fast, obvious
DEFAULT_SIZES = LEETCODE_COMMON_BOUNDS["large"]


class ListNode:
    def __init__(self, val: Optional[int] = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def create_linked_list(
    value: Optional[int] = 0, next: Optional[ListNode] = None
) -> ListNode:
    return ListNode(val=value, next=next)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass


def get_random_int() -> int:
    return np.random.randint()


def main():
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")
    print(f"Random Int: {get_random_int()}")


if __name__ == "__main__":
    main()
