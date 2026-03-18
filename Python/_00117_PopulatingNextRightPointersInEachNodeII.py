from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        """Given a binary tree
        ```
        struct Node {
            int val;
            Node *left;
            Node *right;
            Node *next;
        }
        ```
        Populate each next pointer to point to its next right node. If there is
        no next right node, the next pointer should be set to `NULL`.

        Initially, all next pointers are set to `NULL`.

        Args:
            root (Node): the root of a binary tree

        Returns:
            Node: the binary tree with `next` values assigned
        """

        if not root:
            return None

        curr = root
        dummy = Node()  # sits to the left of the next level
        next_lvl = dummy  # traverses the next level

        while curr:
            # If there is a left node, connect it to the node on its left. If
            # this is the beginning of a level, `dummy` and `next_lvl` are the 
            # same, so setting `next_lvl.next` will aslo set dummy before the 
            # next level. This allows us to advance to the next level.
            if curr.left:
                next_lvl.next = curr.left
                next_lvl = next_lvl.next
            # if there is a right node, connect it to the node on its right.
            if curr.right:
                next_lvl.next = curr.right
                next_lvl = next_lvl.next
            # If there is a node to the right of the current node, advance to it.
            if curr.next:
                curr = curr.next
            else:
                # Otherwise, advance the current node to the next level.
                curr = dummy.next
                # Since the current node is set to `dummy.next` to advance to
                # the next level, `dummy.next` must be null when there are no
                # more levels to prevent an infinite loop.
                dummy.next = None
                next_lvl = dummy

        return root


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def compare(self, t1: "Node | None", t2: "Node | None") -> bool:
        if t1 and not t2 or t2 and not t1:
            return False
        elif not t1 and not t2:
            return True
        if t1.next and not t2.next or t2.next and not t1.next:
            return False

        assert t1 and t2
        if t1.val != t2.val:
            return False

        if t1.next and t2.next and t1.next.val != t2.next.val:
            return False

        return self.compare(t1.left, t2.left) and self.compare(t1.right, t2.right)

    def test_example1(self):
        root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node7 = Node(7)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node2.next = node3
        node3.right = node7
        node4.next = node5
        node5.next = node7

        expected = node1
        actual = self.sol.connect(root)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        root = None
        node1 = None

        expected = node1
        actual = self.sol.connect(root)

        self.assertTrue(self.compare(expected, actual))


if __name__ == "__main__":
    unittest.main()
