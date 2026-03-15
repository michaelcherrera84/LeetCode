from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """Given the `head` of a singly linked list and two integers `left` and
        `right` where `left <= right`, reverse the nodes of the list from
        position `left` to position `right`, and return *the reversed list*.

        Args:
            head (Optional[ListNode]): head of a singly linked list
            left (int): left edge of sublist to be reversed
            right (int): right edge of sublist to be reversed

        Returns:
            Optional[ListNode]: a list with a portion reversed
        """

        # The dummy node lies outside the list and points to the list.
        dummy = ListNode(0, head)
        prev = dummy

        # Put the prev node at the position before `left`
        for _ in range(left - 1):
            prev = prev.next if prev else None

        # Make `curr` the node at position `left`
        curr = prev.next if prev else None

        # Shift `curr` to the right until the node after `curr` is in the
        # position after `right`. Do this by moving the node after `curr` to 
        # the beginning of range.
        for _ in range(right - left):
            assert curr and prev
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def compare(self, a: "ListNode | None", b: "ListNode | None") -> bool:
        while a or b:
            if a and not b:
                return False
            if b and not a:
                return False

            if a and b:
                if a.val != b.val:
                    return False
                a = a.next
                b = b.next

        return True

    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        left = 2
        right = 4
        expected = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        actual = self.sol.reverseBetween(head, left, right)
        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        head = ListNode(5)
        left = 1
        right = 1
        expected = ListNode(5)
        actual = self.sol.reverseBetween(head, left, right)
        self.assertTrue(self.compare(expected, actual))

    def test_example3(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
        left = 1
        right = 8
        expected = ListNode(8, ListNode(7, ListNode(6, ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))))
        actual = self.sol.reverseBetween(head, left, right)
        self.assertTrue(self.compare(expected, actual))


if __name__ == "__main__":
    unittest.main()
