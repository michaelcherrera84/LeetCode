const { _Node, cloneGraph } = require("../src/_00133_CloneGraph");

function buildGraph(adjList) {
    if (!adjList) return null;

    const nodes = [];
    for (let i = 0; i < adjList.length; i++) {
        nodes.push(new _Node(i + 1));
    }

    for (let i = 0; i < adjList.length; i++) {
        for (const val of adjList[i]) {
            nodes[i].neighbors.push(nodes[val - 1]);
        }
    }

    return nodes[0];
}

function graphToAdjList(node) {
    if (!node) return [];

    const adj = {};
    const queue = [node];
    const visited = new Set();

    while (queue.length > 0) {
        const curr = queue.shift();

        if (visited.has(curr.val)) continue;
        visited.add(curr.val);

        adj[curr.val] = curr.neighbors.map((n) => n.val).sort((a, b) => a - b);

        for (const nei of curr.neighbors) {
            if (!visited.has(nei.val)) {
                queue.push(nei);
            }
        }
    }

    // build result array
    const maxVal = Math.max(...Object.keys(adj).map(Number), 0);
    const result = Array.from({ length: maxVal }, () => []);

    for (const val of Object.keys(adj)
        .map(Number)
        .sort((a, b) => a - b)) {
        result[val - 1] = adj[val];
    }

    return result;
}

test("Example 1", () => {
    const adjList = [
        [2, 4],
        [1, 3],
        [2, 4],
        [1, 3],
    ];
    const originalNode = buildGraph(adjList);
    const clonedNode = cloneGraph(originalNode);

    const result = graphToAdjList(clonedNode);
    expect(result).toEqual(adjList);
});

test("Example 2", () => {
    const adjList = [[]];
    const originalNode = buildGraph(adjList);
    const clonedNode = cloneGraph(originalNode);

    const result = graphToAdjList(clonedNode);
    expect(result).toEqual(adjList);
});

test("Example 3", () => {
    const adjList = [];
    const originalNode = buildGraph(adjList);
    const clonedNode = cloneGraph(originalNode);

    const result = graphToAdjList(clonedNode);
    expect(result).toEqual(adjList);
});
