from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """A linked list of length `n` is given such that each node contains an
        additional random pointer, which could point to any node in the list, or
        `null`.

        Construct a **deep copy** of the list. The deep copy should consist of
        exactly `n` **brand new** nodes, where each new node has its value set
        to the value of its corresponding original node. Both the `next` and
        `random` pointer of the new nodes should point to new nodes in the
        copied list such that the pointers in the original list and copied list
        represent the same list state. **None of the pointers in the new list
        should point to nodes in the original list**.

        For example, if there are two nodes `X` and `Y` in the original list,
        where `X.random --> Y`, then for the corresponding two nodes x and y in
        the copied list, `x.random --> y`.

        Return *the head of the copied linked list*.

        The linked list is represented in the input/output as a list of `n`
        nodes. Each node is represented as a pair of `[val, random_index]`
        where:

        - `val`: an integer representing `Node.val`
        - `random_index`: the index of the node (range from `0` to `n-1`) that
        the `random` pointer points to, or `null` if it does not point to any
        node.

        - Your code will `only` be given the head of the original linked list.

        Args:
            head (Optional[Node]): the head of the linked list

        Returns:
            Optional[Node]: a copy of the linked list
        """

        node = head

        # Insert a copy of each node after each node in the list, and make the
        # copy point to the next node in the list.
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next

        node = head

        # Now that each node points to a copy of itself, the random for each 
        # node will point to a node that points to the correct copy, so we can 
        # set the random of each copy, to the copy that is pointed to, by the 
        # random of each node. 
        while node:
            assert node.next is not None
            if node.random:
                node.next.random = node.random.next

            node = node.next.next

        node = head
        copy_head = head.next if head else None

        # Build the copy by pointing to every other node (1, 3, 5, etc), 
        # while fixing the original by skipping the copies (0, 2, 4, etc.)
        while node and node.next:
            copy = node.next
            node.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            node = node.next

        return copy_head


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def compare(self, a: "Node | None", b: "Node | None") -> bool:
        map_a = {}
        map_b = {}

        i = 0
        cur = a
        while cur:
            map_a[cur] = i
            cur = cur.next
            i += 1

        i = 0
        cur = b
        while cur:
            map_b[cur] = i
            cur = cur.next
            i += 1

        while a and b:
            if a.val != b.val:
                return False
            if a is b:
                return False
            if a.random and b.random and a.random is b.random:
                return False

            ra = map_a.get(a.random, None)
            rb = map_b.get(b.random, None)

            if ra != rb:
                return False

            a = a.next
            b = b.next

        return a is None and b is None

    def test_example1(self):
        spec = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

        nodes = [Node(val) for val, _ in spec]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        for i, (_, rand_index) in enumerate(spec):
            if rand_index is not None:
                nodes[i].random = nodes[rand_index]

        head = nodes[0]
        copy = self.sol.copyRandomList(head)
        self.assertTrue(self.compare(head, copy))

    def test_example2(self):
        spec = [[1, 1], [2, 1]]

        nodes = [Node(val) for val, _ in spec]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        for i, (_, rand_index) in enumerate(spec):
            if rand_index is not None:
                nodes[i].random = nodes[rand_index]

        head = nodes[0]
        copy = self.sol.copyRandomList(head)
        self.assertTrue(self.compare(head, copy))

    def test_example3(self):
        spec = [[3, None], [3, 0], [3, None]]

        nodes = [Node(val) for val, _ in spec]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        for i, (_, rand_index) in enumerate(spec):
            if rand_index is not None:
                nodes[i].random = nodes[rand_index]

        head = nodes[0]
        copy = self.sol.copyRandomList(head)
        self.assertTrue(self.compare(head, copy))


if __name__ == "__main__":
    unittest.main()
