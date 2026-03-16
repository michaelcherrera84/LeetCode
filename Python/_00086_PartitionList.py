from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """Given the `head` of a linked list and a value `x`, partition it such
        that all nodes **less than** `x` come before nodes **greater than or
        equal** to `x`.

        You should **preserve** the original relative order of the nodes in
        each of the two partitions.

        Args:
            head (Optional[ListNode]): the head of a linked list
            x (int): value on which to partition the list

        Returns:
            Optional[ListNode]: list which all nodes less `x` come before nodes
            greater than or equal to `x`
        """

        # list of nodes less than `x`
        less_head = less = ListNode(0) 
        # list of nodes greater than or equal to `x`
        greater_head = greater = ListNode(0)  

        curr = head
        # Add each node less than `x` to the less list and each node greater
        # than or equal to `x` to the greater list.
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        # Terminate the list.
        greater.next = None
        # Connect the less list to the front of the greater list.
        less.next = greater_head.next

        return less_head.next


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def build_list(self, arr):
        dummy = ListNode(0)
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

    def compare(self, l1, l2) -> bool:
        while l1 or l2:
            if l1 and not l2 or l2 and not l1:
                return False

            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        return True

    def test_example1(self):
        input = [1, 4, 3, 2, 5, 2]
        x = 3
        output = [1, 2, 2, 4, 3, 5]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.partition(head, x)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        input = [2, 1]
        x = 2
        output = [1, 2]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.partition(head, x)

        self.assertTrue(self.compare(expected, actual))


if __name__ == "__main__":
    unittest.main()
