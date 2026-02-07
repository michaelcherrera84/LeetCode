const { TreeNode, hasPathSum } = require("../src/_00112_PathSum");

test("example1", () => {
    const root = new TreeNode(
        5,
        new TreeNode(4, new TreeNode(11, new TreeNode(7), new TreeNode(2))),
        new TreeNode(8, new TreeNode(13), new TreeNode(4, null, new TreeNode(1))),
    );

    expect(hasPathSum(root, 22)).toBe(true);
});

test("example2", () => {
    const root = new TreeNode(1, new TreeNode(2), new TreeNode(3));

    expect(hasPathSum(root, 5)).toBe(false);
});

test("example3 (empty tree does not have target sum)", () => {
    expect(hasPathSum(null, 0)).toBe(false);
});

test("root with left node null and root equals target does not have target sum", () => {
    const root = new TreeNode(1, new TreeNode(2));

    expect(hasPathSum(root, 1)).toBe(false);
});

test("tree with one node equal to target sum has target sum", () => {
    const root = new TreeNode(1);

    expect(hasPathSum(root, 1)).toBe(true);
});

test("one sided tree with target sum in middel does not have targer sum", () => {
    const root = new TreeNode(1, new TreeNode(2, new TreeNode(3, new TreeNode(4, new TreeNode(5)))));

    expect(hasPathSum(root, 6)).toBe(false);
});
