from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        node = self
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next.val if self.next else None})"


class Solution:
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the `head` of a linked list, return *the list after sorting it in
        **ascending order***.

        Args:
            head (Optional[ListNode]): the head of a singly-linked list

        Returns:
            Optional[ListNode]: the list sorted
        """

        def merge(l1, l2):
            """
            Sort and merge two sections of a linked list.

            Args:
                l1 (ListNode): a section of a linked list
                l2 (ListNode): a section of a linked list

            Returns:
                ListNode: the sorted merged list
            """
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            curr.next = l1 if l1 else l2
            return dummy.next

        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        # Find the middle of the list by advancing fast twice as fast as slow.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Separate the sections of the list.
        mid = slow.next
        slow.next = None

        # Continue separating sections of the list recursively until the
        # sections are only a single node, then begin recombining the nodes
        # in order and returning the sorted combined sections until the full
        # list is combined in the original method call.
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the `head` of a linked list, return *the list after sorting it in
        **ascending order***.

        Args:
            head (Optional[ListNode]): the head of a singly-linked list

        Returns:
            Optional[ListNode]: the list sorted
        """

        as_list = []
        curr = head
        
        # Create a list from the linked list.
        while curr:
            as_list.append(curr.val)
            curr = curr.next

        as_list.sort() # Sort the list.

        curr = head
        
        # Set the values of the linked list from the sorted list.
        for val in as_list:
            curr.val = val
            curr = curr.next

        return head


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def build_linked(self, as_list):
        dummy = ListNode()
        node = dummy

        for item in as_list:
            node.next = ListNode(item)
            node = node.next

        return dummy.next

    def build_list(self, root):
        node = root
        res = []

        while node:
            res.append(node.val)
            node = node.next

        return res

    def test_example1(self):
        input = [4, 2, 1, 3]
        expected = sorted(input)

        head = self.build_linked(input)
        actual = self.sol.sortList(head)
        output = self.build_list(actual)

        self.assertEqual(expected, output)

    def test_example2(self):
        input = [-1, 5, 3, 4, 0]
        expected = sorted(input)

        head = self.build_linked(input)
        actual = self.sol.sortList(head)
        output = self.build_list(actual)

        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
