// Definition for a _Node.
function _Node(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
}

/**
 * Given a reference of a node in a connected undirected graph, return a deep
 * copy (clone) of the graph.
 *
 * Each node in the graph contains a value (`int`) and a list (`List[Node]`) of
 * its neighbors.
 *
 * ```java
 * class Node {
 *     public int val;
 *     public List<Node> neighbors;
 * }
 * ```
 *
 * **Test case format**:
 *
 * For simplicity, each node's value is the same as the node's index (1-indexed).
 * For example, the first node with `val == 1`, the second node with `val == 2`,
 * and so on. The graph is represented in the test case using an adjacency list.
 *
 * **An adjacency list** is a collection of unordered **lists** used to represent
 * a finite graph. Each list describes the set of neighbors of a node in the graph.
 *
 * The given node will always be the first node with `val = 1`. You must return
 * the **copy of the given node** as a reference to the cloned graph.
 * @param {_Node} node a reference of a node in a connected undirected graph
 * @return {_Node} the copy of the given node as a reference to the cloned graph
 */
var cloneGraph = function (node) {
    if (!node) return null;

    // Since each node can be a neighbor to any number of other nodes, we will
    // maintain a map of each cloned node for quick access.
    const clones = new Map();

    /**
     * Clone the graph using DFS to clone the neighbors lists.
     * @param {_Node} n a node to clone
     * @returns the cloned node
     */
    function cloneNodes(n) {
        // If we have already cloned this node, fetch it from the map.
        if (clones.has(n.val)) return clones.get(n.val);

        // Create a new clone with this node's value and add the clone to the map.
        const clone = new _Node(n.val);
        clones.set(n.val, clone);

        // Build the clone's neighbors list recursively.
        for (neighbor of n.neighbors) {
            clone.neighbors.push(cloneNodes(neighbor));
        }

        return clone;
    }

    return cloneNodes(node);
};

module.exports = { _Node, cloneGraph };
