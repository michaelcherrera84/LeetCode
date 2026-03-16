from collections import deque


class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.
    """

    def __init__(self, capacity: int):
        """Initialize the LRU cache with **positive** size `capacity`.

        Args:
            capacity (int): the capacity of the LRU cache
        """
        self.capacity = capacity
        self.cache: dict[int, ListNode] = {}

        # The list will exists between these dummy nodes.
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        """Remove a node from the list.

        Args:
            node (ListNode): the node to remove
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_tail(self, node: ListNode) -> None:
        """Insert a node at the end of the list

        Args:
            node (ListNode): the node to insert
        """
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        """Return the value of the `key` if the key exists otherwise return `-1`.

        Args:
            key (int): the key to search for

        Returns:
            int: the value of the `key` if the key exists, otherwise `-1`
        """

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        # Remove the node from it current postion to place it at the end of the
        # the list to become the LRU.
        self._remove(node)
        self._insert_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """Update the value of the `key` if the `key` exists. Otherwise, add the
        `key-value` pair to the cache. If the number of keys exceeds the
        `capacity` from this operation, **evict** the least recently used key.

        Args:
            key (int): the key to update
            value (int): the new value of the key
        """

        # If the key exists, remove the current version from the list.
        if key in self.cache:
            self._remove(self.cache[key])

        node = ListNode(key, value)
        self.cache[key] = node  # Update the cache.
        self._insert_tail(node)  # Add the new version to the end of the list.

        # If the capacity is exceeded, remove the node at the beginning of the
        # list (LRU) and its corresponding key from the cache.
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


import unittest


class Test_Solution(unittest.TestCase):
    def test_example1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(1, lRUCache.get(1))
        lRUCache.put(3, 3)
        self.assertEqual(-1, lRUCache.get(2))
        lRUCache.put(4, 4)
        self.assertEqual(-1, lRUCache.get(1))
        self.assertEqual(3, lRUCache.get(3))
        self.assertEqual(4, lRUCache.get(4))


if __name__ == "__main__":
    unittest.main()
