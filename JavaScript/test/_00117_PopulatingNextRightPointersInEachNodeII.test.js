const { _Node, connect } = require("../src/_00117_PopulatingNextRightPointersInEachNodeII");

function compare(t1, t2) {
    if ((t1 && !t2) || (t2 && !t1)) return false;
    if (!t1 && !t2) return true;
    if ((t1.next && !t2.next) || (t2.next && !t1.next)) return false;
    if (t1.val != t2.val) return false;
    if (t1.next && t2.next && t1.next.val != t2.next.val) return false;
    return compare(t1.left, t2.left) && compare(t1.right, t2.right);
}

test("Example 1", () => {
    const root = new _Node(1, new _Node(2, new _Node(4), new _Node(5)), new _Node(3, null, new _Node(7)));

    const node1 = new _Node(1);
    const node2 = new _Node(2);
    const node3 = new _Node(3);
    const node4 = new _Node(4);
    const node5 = new _Node(5);
    const node7 = new _Node(7);

    node1.left = node2;
    node1.right = node3;
    node2.left = node4;
    node2.right = node5;
    node2.next = node3;
    node3.right = node7;
    node4.next = node5;
    node5.next = node7;

    const expected = node1;
    const actual = connect(root);

    expect(compare(expected, actual)).toBe(true);
});
