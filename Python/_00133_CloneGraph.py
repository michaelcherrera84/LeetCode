# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """Given a reference of a node in a connected undirected graph, return a
        deep copy (clone) of the graph.

        Each node in the graph contains a value (`int`) and a list (`List[Node]`)
        of its neighbors.

        ```
        class Node {
            public int val;
            public List<Node> neighbors;
        }
        ```

        **Test case format:**

        For simplicity, each node's value is the same as the node's index
        (1-indexed). For example, the first node with `val == 1`, the second
        node with `val == 2`, and so on. The graph is represented in the test
        case using an adjacency list.

        **An adjacency list** is a collection of unordered **lists** used to
        represent a finite graph. Each list describes the set of neighbors of a
        node in the graph.

        The given node will always be the first node with `val = 1`. You must
        return the **copy of the given node** as a reference to the cloned graph.

        Args:
            node (Node): reference of a node in a connected undirected graph

        Returns:
            Node: a clone of the graph
        """
        if not node:
            return None

        clones = {node.val: Node(node.val)}  # map of copied nodes
        queue = deque([node])  # nodes remaining to finish copying

        # While there are nodes to copy...
        while queue:
            # Get the next node that still needs its neighbors list copied.
            curr = queue.popleft()
            # Get the copy of this node from the map.
            copy = clones[curr.val]

            # Copy the neighbors list from this node to the copy node
            for neighbor in curr.neighbors:
                # If the clone of this neighbor has not been created, create it
                # and add it to the map. Then add this node to the queue so that
                # we copy its neighbors list.
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                # Append this new clone to the copy's neighbors list.
                copy.neighbors.append(clones[neighbor.val])

        return clones[1]


import unittest
from typing import List


class Test_Solution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def build_graph(self, adjList: List[List[int]]) -> Optional[Node]:
        """Build graph from LeetCode-style adjacency list and return node with val=1."""
        if not adjList:
            return None

        nodes = [Node(i + 1) for i in range(len(adjList))]

        for i, neighbors in enumerate(adjList):
            for nei_val in neighbors:
                nodes[i].neighbors.append(nodes[nei_val - 1])

        return nodes[0]  # node with val = 1


    def graph_to_adj_list(self, node: Optional[Node]) -> List[List[int]]:
        """Convert cloned graph back to adjacency list for comparison."""
        if not node:
            return []

        adj = {}
        queue = deque([node])
        visited = set()

        while queue:
            curr = queue.popleft()
            if curr.val in visited:
                continue
            visited.add(curr.val)

            # sort for consistent comparison
            adj[curr.val] = sorted([n.val for n in curr.neighbors])  

            for nei in curr.neighbors:
                if nei.val not in visited:
                    queue.append(nei)

        # Return list in order of val 1, 2, 3, ...
        max_val = max(adj.keys()) if adj else 0
        result = [[] for _ in range(max_val)]
        for val in sorted(adj.keys()):
            result[val - 1] = adj[val]

        return result

    def test_example1(self):
        adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original_node = self.build_graph(adjList)
        cloned_node = self.sol.cloneGraph(original_node)

        result = self.graph_to_adj_list(cloned_node)
        self.assertEqual(result, adjList)

    def test_single_node(self):
        adjList = [[]]
        original_node = self.build_graph(adjList)
        cloned_node = self.sol.cloneGraph(original_node)

        result = self.graph_to_adj_list(cloned_node)
        self.assertEqual(result, adjList)

    def test_two_nodes(self):
        adjList = [[2], [1]]
        original_node = self.build_graph(adjList)
        cloned_node = self.sol.cloneGraph(original_node)

        result = self.graph_to_adj_list(cloned_node)
        self.assertEqual(result, adjList)

    def test_empty(self):
        self.assertIsNone(self.sol.cloneGraph(None))


if __name__ == "__main__":
    unittest.main()
