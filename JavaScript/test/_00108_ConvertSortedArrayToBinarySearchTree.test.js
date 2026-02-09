const { TreeNode, sortedArrayToBST } = require("../src/_00108_ConvertSortedArrayToBinarySearchTree");

function isSameTree(p, q) {
    if (p === null && q === null) return true;
    if (p === null || q === null) return false;
    if (p.val !== q.val) return false;

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

test("example1", () => {
    const nums = [-10, -3, 0, 5, 9];
    const expected = new TreeNode(0, new TreeNode(-10, null, new TreeNode(-3)), new TreeNode(5, null, new TreeNode(9)));
    expect(isSameTree(expected, sortedArrayToBST(nums))).toBe(true);
});

test("example2", () => {
    const nums = [1, 3];
    const expected = new TreeNode(1, null, new TreeNode(3));
    expect(isSameTree(expected, sortedArrayToBST(nums))).toBe(true);
});

test("[-1,0,3,5,9,12,20,33,45,67] as a BST is [12,3,45,0,9,33,67,-1,null,5,null,20]", () => {
    const nums = [-1, 0, 3, 5, 9, 12, 20, 33, 45, 67];
    const expected = new TreeNode(
        9,
        new TreeNode(0, new TreeNode(-1), new TreeNode(3, null, new TreeNode(5))),
        new TreeNode(33, new TreeNode(12, null, new TreeNode(20)), new TreeNode(45, null, new TreeNode(67))),
    );
    expect(isSameTree(expected, sortedArrayToBST(nums))).toBe(true);
});
