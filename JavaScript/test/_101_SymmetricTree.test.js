const { TreeNode, isSymmetric } = require("../src/_101_SymmetricTree");

test("example1", () => {
    const root = new TreeNode(
        1,
        new TreeNode(2, new TreeNode(3), new TreeNode(4)),
        new TreeNode(2, new TreeNode(4), new TreeNode(3)),
    );

    expect(isSymmetric(root)).toBe(true);
});

test("example2", () => {
    const root = new TreeNode(1, new TreeNode(2, null, new TreeNode(3)), new TreeNode(2, null, new TreeNode(3)));

    expect(isSymmetric(root)).toBe(false);
});

test("single node is symmetric", () => {
    const root = new TreeNode(1);

    expect(isSymmetric(root)).toBe(true);
});

test("tree with no nodes on one side is not symmetric", () => {
    const root = new TreeNode(1, null, new TreeNode(3));

    expect(isSymmetric(root)).toBe(false);
});

test("tree with more nodes on one side than the other is not symmetric", () => {
    const root = new TreeNode(1, new TreeNode(2), new TreeNode(2, null, new TreeNode(3)));

    expect(isSymmetric(root)).toBe(false);
});
