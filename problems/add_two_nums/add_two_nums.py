import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l2:
            return l1

        output = ListNode()

        assert isinstance(l1, ListNode), f"Expect {type(l1)} is ListNode"
        assert isinstance(l2, ListNode), f"Expect {type(l1)} is ListNode"

        while l1.next and l2.next:
            output.val = l1.val + l2.val
            l1, l2 = l1.next, l2.next
            output.next = ListNode()

        output.val = l1.val + l2.val

        return output


def add_node(L: ListNode | None = None, value: int | None = None) -> ListNode:

    if not L:
        return ListNode()

    if not value:
        return ListNode()

    L.next = ListNode(val=value)
    return L


def is_end(L: ListNode | None = None) -> bool | None:
    if L is None:
        return None

    if L.next is None:
        return True
    return False


def step_forward(node: ListNode) -> ListNode | None:
    L = copy.deepcopy(node)
    if L.next is None:
        return L
    return L.next


def main():
    left = ListNode(val=1)
    right = ListNode(val=2)
    left = add_node(left, 3)
    right = add_node(right, 4)
    left = add_node(left, 5)
    right = add_node(right, 6)

    continue_left = not is_end(left)
    continue_right = not is_end(right)

    while continue_left and continue_right:
        # get values
        if left.val is None:
            break

        if right.val is None:
            break

        print(f"Left: {left.val} | Right: {right.val}")
        left = left.next
        right = right.next
        continue_left = left is not None
        continue_right = right is not None

    print(f"Left: {left.val} | Right: {right.val}")


if __name__ == "__main__":
    main()
