from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given the `head` of a sorted linked list, *delete all nodes that have 
        duplicate numbers, leaving only distinct numbers from the original list*. 
        Return *the linked list **sorted** as well*.

        Args:
            head (Optional[ListNode]): the head of a sorted linked list

        Returns:
            Optional[ListNode]: sorted linked list without duplicated nodes
        """

        dummy = ListNode(0, head)
        curr = dummy.next
        tail = dummy # last non duplicate value


        while curr:
            # If the next value is equal to the current value,...
            if curr.next and curr.val == curr.next.val:
                # advance current until a new value is next.
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Advance to the non-duplicate value.    
                curr = curr.next 
                # Connect the tail to the non-duplicate value.
                tail.next = curr 
            # Otherwise, advance `tail` an `curr`.
            else:
                tail = curr
                curr = curr.next
            
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
        input = [1, 2, 3, 3, 4, 4, 5]
        output = [1, 2, 5]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.deleteDuplicates(head)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        input = [1, 1, 1, 2, 3]
        output = [2, 3]

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.deleteDuplicates(head)

        self.assertTrue(self.compare(expected, actual))

    def test_empty_list(self):
        input = []
        output = []

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.deleteDuplicates(head)

        self.assertTrue(self.compare(expected, actual))

    def test_remove_all(self):
        input = [1, 1, 1, 1]
        output = []

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.deleteDuplicates(head)

        self.assertTrue(self.compare(expected, actual))

    def test_remove_all_different(self):
        input = [1, 1, 2, 2, 3, 3]
        output = []

        head = self.build_list(input)
        expected = self.build_list(output)
        actual = self.sol.deleteDuplicates(head)

        self.assertTrue(self.compare(expected, actual))

if __name__ == "__main__":
    unittest.main()