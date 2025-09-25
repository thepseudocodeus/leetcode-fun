import marimo

__generated_with = "0.16.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Merge Two Sorted Lists

    ## Provided
    - You are given the heads of two sorted linked lists list1 and list2.
    - Merge teh two lists into one sorted list.
    - Make the list by splicing together the nodes of the first two lists.
    - Return teh head of the merged linked list.

    ## Examples

    Scenario:
    1. same length list

        - list1 = 1 -> 2 -> 4, [1, 2, 4]
        - list2 = 1 -> 3 -> 4, [1, 3, 4]

    Input: list1, list2
    Output: list3 = 1 -> 1 -> 2 -> 3 -> 4 -> 4 as [1, 1, 2, 3, 4, 4]

    2. both empty lists

        - list1 = []
        - list2 = []

    Input: list1, list2
    Output: []

    3. one empty list

        - list1 = []
        - list2 = [0]

    Input: list1, list2
    Output: [0]

    ### Constraints

    - Nodes in list [0, 50]
    - 100 * -1 <= Node.val <= 100
    - list1, list2 are sorted in ascending order

   
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Mathematic Definition
    There exists two sets of numbers starting with the number n. The sequence follows a pattern such that n <= n + 1 <= n + 2. Each set is stored in a object consistin of nodes (N).

    Each Node has two features: 1. val and 2. next. Val stores the interger value for the given node. Next points of the next N if it exists of None. This object is known as a linked list because it connects data such that insertion and deletion is an O(1) average time & space compelxity operation.

    We are provided two linked lists with 0 or more integer values. Create a merged list from these two lists that is also sorted in ascending order.

    ## Questions
    - What is ascending order?
    n = None, 0, n + 1, n + 2, n + n

    - How would a Node be represented?
    A node is a 2 feature data structure allowing for O(1) access to these features.


    - How would a Linked list be represented?
    A linked list is a grouping (collection) of Nodes. It should house the head and tail of the object to facilitate O(1) average access to the start and end.


    # Pseudocode
    BEGIN
        dummy = Node()
        OUTPUT = dummy
    
        WHILE LL1 EXISTS AND LL2 EXISTS
            IF LL1 NOT EXIST
                RETURN LL2

            IF LL2 NOT EXIST
                RETURN LL2

            IF LL1.val <= LL2.val
                OUTPUT.next = LL1

            ELSE
                OUTPUT.next = LL2

            OUTPUT = OUTPUT.next

        OUTPUT.next = LL1 IF LL1 is None ELSE LL2
    END

    """
    )
    return


@app.cell
def _():
    import marimo as mo
    from typing import Optional
    return Optional, mo


@app.cell
def _(Optional):
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class LinkedList:
        def __init__(self, node: Optional[ListNode] = None):
            self.head = None
            self.tail = None
            self.current = node


        def __str__(self):
            """String representation of linked list. Learned from geeksforgeeks.com"""
      
            # defining a blank res variable
            res = ""
        
            # initializing ptr to head
            ptr = self.head
        
           # traversing and adding it to res
            while ptr:
                res = ",".join(res, str(ptr.val))
                ptr = ptr.next

           # removing trailing commas
            res = res.strip(", ")
        
            # chen checking if 
            # anything is present in res or not
            if len(res):
                return "[" + res + "]"
            else:
                return "[]"
    return LinkedList, ListNode


@app.cell
def _(LinkedList, ListNode, Optional):
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # return list2 if list1 = None
            if not list1:
                return list2

            if not list2:
                return list1

            output = LinkedList(ListNode())

            while list1 and list2:
                if list1.val <= list2.val:
                    output.current = list1
                    list1 = list1.next
                else:
                    output.current = list2
                    list2 = list2.next
            
                output.head = output.current

            return output.head
                
    return (Solution,)


@app.cell
def _(ListNode):
    L1 = ListNode(1, ListNode(2, ListNode(4)))
    L2 = ListNode(1, ListNode(3, ListNode(4)))
    return L1, L2


@app.cell
def _(L1, L2, Solution):
    s = Solution()
    results = s.mergeTwoLists(L1, L2)
    print(results)
    return


if __name__ == "__main__":
    app.run()
