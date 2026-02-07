const { TreeNode, averageOfLevels } = require("../src/_637_AverageOfLevelsInBinaryTree");

test("example1", () => {
    const root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
    const expected = [3.0, 14.5, 11.0];
    const actual = averageOfLevels(root);

    expect(actual).toHaveLength(expected.length);

    for (let i = 0; i < actual.length; i++) {
        expect(actual[i]).toBeCloseTo(expected[i], 5);
    }
});

test("example2", () => {
    const root = new TreeNode(3, new TreeNode(9, new TreeNode(15), new TreeNode(7)), new TreeNode(20));
    const expected = [3.0, 14.5, 11.0];
    const actual = averageOfLevels(root);

    expect(actual).toHaveLength(expected.length);

    for (let i = 0; i < actual.length; i++) {
        expect(actual[i]).toBeCloseTo(expected[i], 5);
    }
});

test("tree with node has average of that node", () => {
    const root = new TreeNode(5);
    expect(averageOfLevels(root)).toStrictEqual([5]);
})

test("if all nodes have max int the average is max int", () => {
    const root = new TreeNode(2147483647, new TreeNode(2147483647), new TreeNode(2147483647));
    const expected = [2147483647, 2147483647];
    const actual = averageOfLevels(root);

    expect(actual).toHaveLength(expected.length);

    for (let i = 0; i < actual.length; i++) {
        expect(actual[i]).toBeCloseTo(expected[i], 5);
    }
})