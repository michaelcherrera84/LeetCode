const { TreeNode, countNodes } = require("../src/_222_CountCompleteTreeNodes");

test("example1", () => {
    const root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3, new TreeNode(6)));
    expect(countNodes(root)).toBe(6);
});

test("example2 (empty tree has 0 nodes)", () => {
    expect(countNodes(null)).toBe(0);
});

test("example3 (tree with 1 node has 1 node", () => {
    const root = new TreeNode(1);
    expect(countNodes(root)).toBe(1);
});

test("even tree with 3 nodes has 3 nodes", () => {
    const root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
    expect(countNodes(root)).toBe(3);
});

test("tree with 2 nodes has 2 nodes", () => {
    const root = new TreeNode(1, new TreeNode(2));
    expect(countNodes(root)).toBe(2);
});
