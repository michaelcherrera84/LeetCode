const { TreeNode, invertTree } = require("../src/_00226_InvertBinaryTree");

function isSameTree(p, q) {
    if (p === null && q === null) return true;
    if (p === null || q === null) return false;
    if (p.val !== q.val) return false;

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

test("example1", () => {
    const root = new TreeNode(
        4,
        new TreeNode(2, new TreeNode(1), new TreeNode(3)),
        new TreeNode(7, new TreeNode(6), new TreeNode(9)),
    );

    const expected = new TreeNode(
        4,
        new TreeNode(7, new TreeNode(9), new TreeNode(6)),
        new TreeNode(2, new TreeNode(3), new TreeNode(1)),
    );

    const result = invertTree(root);

    expect(isSameTree(result, expected)).toBe(true);
});

test("example2", () => {
    const root = new TreeNode(2, new TreeNode(1), new TreeNode(3));
    const expected = new TreeNode(2, new TreeNode(3), new TreeNode(1));

    const result = invertTree(root);

    expect(isSameTree(result, expected)).toBe(true);
});

test("empty tree stays null", () => {
    expect(invertTree(null)).toBe(null);
});
