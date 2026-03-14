from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """You are given two **non-empty** linked lists representing two
        non-negative integers. The digits are stored in **reverse order**, and
        each of their nodes contains a single digit. Add the two numbers and
        return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except
        the number 0 itself.

        Args:
            l1 (Optional[ListNode]): first number
            l2 (Optional[ListNode]): second number

        Returns:
            Optional[ListNode]: sum of the numbers
        """

        top = l1  # to traverse the top "number"
        bottom = l2  # to traverse the bottom "number"
        res = ListNode()  # dummy node to point to the sum

        curr = res  # to add to the sum
        carry = 0

        # While there are numbers to add...
        while top or bottom or carry:
            a = top.val if top else 0
            b = bottom.val if bottom else 0
            c = a + b + carry

            carry = c // 10
            curr.next = ListNode(c % 10) 

            if top:
                top = top.next
            if bottom:
                bottom = bottom.next
            curr = curr.next

        return res.next


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def to_list(self, node):
        """Helper to convert a linked list to a Python list."""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_example1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        expected = ListNode(7, ListNode(0, ListNode(8)))
        actual = self.sol.addTwoNumbers(l1, l2)
        assert self.to_list(expected) == self.to_list(actual)

    def test_example2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        expected = ListNode(0)
        actual = self.sol.addTwoNumbers(l1, l2)
        assert self.to_list(expected) == self.to_list(actual)

    def test_example3(self):
        l1 = ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
            ),
        )
        l2 = ListNode(
            9,
            ListNode(
                9,
                ListNode(
                    9,
                    ListNode(
                        9,
                    ),
                ),
            ),
        )
        expected = ListNode(
            8,
            ListNode(
                9,
                ListNode(
                    9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
                ),
            ),
        )
        actual = self.sol.addTwoNumbers(l1, l2)
        assert self.to_list(expected) == self.to_list(actual)


if __name__ == "__main__":
    unittest.main()
