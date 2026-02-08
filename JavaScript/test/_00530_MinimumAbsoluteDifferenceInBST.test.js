const { TreeNode, getMinimumDifference } = require("../src/_00530_MinimumAbsoluteDifferenceInBST");

test("example1", () => {
    const root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(6));
    expect(getMinimumDifference(root)).toBe(1);
})

test("example2", () => {
    const root = new TreeNode(1, new TreeNode(0), new TreeNode(48, new TreeNode(12), new TreeNode(49)));
    expect(getMinimumDifference(root)).toBe(1);
})

test("minimum difference of [5, 1] is 4", () => {
    const root = new TreeNode(5, new TreeNode(1));
    expect(getMinimumDifference(root)).toBe(4);
})

test("minimum difference of [100000, 0] is 100000", () => {
    const root = new TreeNode(100000, new TreeNode(0));
    expect(getMinimumDifference(root)).toBe(100000);
})