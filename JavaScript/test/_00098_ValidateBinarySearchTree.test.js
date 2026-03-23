const { TreeNode, isValidBST } = require("../src/_00098_ValidateBinarySearchTree");

function buildTree(input) {
    const root = new TreeNode(input[0]);
    const queue = [root];
    const n = input.length;
    let i = 1;

    while (queue.length > 0 && i < n) {
        const node = queue.shift();

        if (i < n && input[i]) {
            node.left = new TreeNode(input[i]);
            queue.push(node.left);
        }
        i++;

        if (i < n && input[i]) {
            node.right = new TreeNode(input[i]);
            queue.push(node.right);
        }
        i++;
    }

    return root;
}

test("Example 1", () => {
    const input = [2, 1, 3];
    const root = buildTree(input);
    expect(isValidBST(root)).toBe(true);
});

test("Example 2", () => {
    const input = [5, 1, 4, null, null, 3, 6];
    const root = buildTree(input);
    expect(isValidBST(root)).toBe(false);
});
