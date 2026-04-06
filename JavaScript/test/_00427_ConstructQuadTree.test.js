const { _Node, construct } = require("../src/_00427_ConstructQuadTree");

/**
 * Create an array representation of a quad-tree.
 *
 * @param {_Node} root the root of a quad-tree
 */
function toArray(root) {
    const queue = [root];
    let res = [];

    while (queue.length) {
        const node = queue.shift();

        if (node) {
            res.push([node.isLeaf, node.val]);
            queue.push(node.topLeft);
            queue.push(node.topRight);
            queue.push(node.bottomLeft);
            queue.push(node.bottomRight);
        } else {
            res.push(null);
        }
    }

    for (let i = res.length - 1; i >= 0; i--)
        if (res[i]) {
            res = res.slice(0, i + 1);
            break;
        }

    return res;
}

test("Example 1", () => {
    const grid = [
        [0, 1],
        [1, 0],
    ];
    const output = construct(grid);
    const expected = [
        [0, 1],
        [1, 0],
        [1, 1],
        [1, 1],
        [1, 0],
    ];
    const actual = toArray(output);
    expect(actual).toEqual(expected);
});

test("Example 2", () => {
    const grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ];
    const output = construct(grid);
    const expected = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], null, null, null, null, [1, 0], [1, 0], [1, 1], [1, 1]];
    const actual = toArray(output);
    expect(actual).toEqual(expected);
});
