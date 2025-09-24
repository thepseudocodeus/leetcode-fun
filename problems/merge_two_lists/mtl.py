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
from typing import Optional, Tuple, List


class ListNode:
    def __init__(self, val: Optional[int] = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self._merge_lists(list1, list2)

    def _stop_early(self, left, right) -> Tuple[Optional[ListNode], bool]:
        """Check if inputs trigger early exit."""
        if not left and not right:
            return ListNode(), True

        if not left:
            return right, True

        if not right:
            return left, True

        return None, False

    def _merge_lists(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> ListNode:
        """Merge the two linked lists by smallest value."""
        result, should_stop = self._stop_early(left, right)
        if should_stop:
            if result is not None:
                return result

        output: ListNode = ListNode()
        left_exit = right_exit = False
        assert left is not None, "Expect node to exist."
        assert right is not None, "Expect node to exist."
        assert isinstance(left.val, int), f"Expect {type(left.val)} is type int."
        assert isinstance(right.val, int), f"Expect {type(right.val)} is type int."

        while left and right:
            try:
                if left.val <= right.val:
                    tmp = output
                    tmp.next = ListNode(val=left.val)
                    output = tmp
                    left_exit = left.next is None
                    left = left.next
                else:
                    tmp = output
                    tmp.next = ListNode(val=right.val)
                    output = tmp
                    right_exit = right.next is None
                    right = right.next
            except Exception:
                pass

        # if left_exit and right_exit:
        #     return output

        if left_exit:
            output.next = right
            return output

        if right_exit:
            output.next = left
            return output

        return output


def _linked_list_factory(int_list: List[int], acc: ListNode) -> ListNode:
    if not int_list:
        return acc

    tmp = int_list.copy()
    tmp_node = None
    first = None
    second = None
    if tmp[0] and tmp[1]:
        first = tmp.pop()
        second = tmp.pop()
        tmp_node = ListNode(val=first, next=ListNode(val=second))

    if tmp_node is None:
        pass

    if acc.next is None:
        acc = tmp_node

    acc.val = current_value
    return _linked_list_factory(tmp, acc)


def create_llist(int_list: List[int]) -> ListNode:
    tmp = int_list.copy()
    n = ListNode()
    return _linked_list_factory(tmp, n)


def main():
    i1 = [1, 2, 4]
    i2 = [1, 3, 4]
    l1 = create_llist(i1)
    l2 = create_llist(i2)
    s = Solution()
    current = s.mergeTwoLists(l1, l2)

    while current:
        print(f"Value: {current.val}")
        current = current.next


if __name__ == "__main__":
    main()
