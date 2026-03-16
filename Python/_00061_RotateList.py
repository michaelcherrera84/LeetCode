from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Given the `head` of a linked list, rotate the list to the right by
        `k` places.

        Args:
            head (Optional[ListNode]): the head of the linked list
            k (int): number of places to rotate the list

        Returns:
            Optional[ListNode]: the rotated list
        """

        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head

        # Find the length and the end of the list.
        while tail.next:
            tail = tail.next
            n += 1

        # Skip complete rotations
        k = k % n
        if k == 0:
            return head

        # Fine the tail and head of the rotated list.
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next if new_tail else None
        new_head = new_tail.next if new_tail else None

        # Move the old tail to the beginning of the old list.
        tail.next = head

        # Terminate the rotated list.
        if new_tail:
            new_tail.next = None

        return new_head


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
        input = [1, 2, 3, 4, 5]
        k = 2
        output = [4, 5, 1, 2, 3]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.rotateRight(head, k)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        input = [0, 1, 2]
        k = 4
        output = [2, 0, 1]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.rotateRight(head, k)

        self.assertTrue(self.compare(expected, actual))

    def test_example3(self):
        input = []
        k = 0
        output = []

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.rotateRight(head, k)

        self.assertTrue(self.compare(expected, actual))

    def test_example4(self):
        input = [1, 2]
        k = 2
        output = [1, 2]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.rotateRight(head, k)

        self.assertTrue(self.compare(expected, actual))


if __name__ == "__main__":
    unittest.main()
