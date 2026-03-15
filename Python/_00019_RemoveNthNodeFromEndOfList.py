from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Given the `head` of a linked list, remove the `nth` node from the end
        of the list and return its head.

        Args:
            head (Optional[ListNode]): head of a linked list
            n (int): node from the end of the list to remove

        Returns:
            Optional[ListNode]: the list with the node removed
        """

        dummy = ListNode(0, head)  # node added before the list
        fast = dummy  # node to traverse the list

        # Advance `fast` so that it will be `n + 1` nodes ahead of `slow`
        for _ in range(n + 1):
            fast = fast.next if fast else None

        slow = dummy  # `n + 1` behind `fast`

        # When `fast` advances past the end of the list, `slow` will be on the
        # node before the node to be deleted.
        while fast and slow:
            fast = fast.next
            slow = slow.next

        # Connect the node before the `nth` to the node after the `nth`
        if slow and slow.next:
            slow.next = slow.next.next

        return dummy.next


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def build_list(self, array):
        dummy = ListNode(0)
        tail = dummy

        for val in array:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next

    def compare(self, l1, l2):
        while l1 or l2:
            if l1 and not l2 or l2 and not l1:
                return False
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True

    def test_example1(self):
        input = [1, 2, 3, 4, 5]
        n = 2
        output = [1, 2, 3, 5]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.removeNthFromEnd(head, n)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        input = [1]
        n = 1
        output = []

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.removeNthFromEnd(head, n)

        self.assertTrue(self.compare(expected, actual))

    def test_example3(self):
        input = [1, 2]
        n = 1
        output = [1]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.removeNthFromEnd(head, n)

        self.assertTrue(self.compare(expected, actual))

    def test_remove_first(self):
        input = [1, 2]
        n = 2
        output = [2]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.removeNthFromEnd(head, n)

        self.assertTrue(self.compare(expected, actual))


if __name__ == "__main__":
    unittest.main()
