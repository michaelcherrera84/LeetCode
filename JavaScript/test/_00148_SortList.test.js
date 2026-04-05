const { ListNode, sortList } = require("../src/_00148_SortList");

function build_list(array) {
    if (array.length == 0) return null;
    const head = new ListNode(array[0]);
    let node = head;

    for (let i = 1; i < array.length; i++) {
        node.next = new ListNode(array[i]);
        node = node.next;
    }

    return head;
}

function to_array(node) {
    res = [];

    while (node) {
        res.push(node.val);
        node = node.next;
    }

    return res;
}

test("Example 1", () => {
    const input = [4, 2, 1, 3];
    const expected = Array.from(input).sort();

    const head = build_list(input);
    const actual = sortList(head);
    const output = to_array(actual);

    expect(output).toEqual(expected);
});

test("Example 2", () => {
    const input = [-1, 5, 3, 4, 0];
    const expected = Array.from(input).sort();

    const head = build_list(input);
    const actual = sortList(head);
    const output = to_array(actual);

    expect(output).toEqual(expected);
});

test("Example 3", () => {
    const input = [];
    const expected = Array.from(input).sort();

    const head = build_list(input);
    const actual = sortList(head);
    const output = to_array(actual);

    expect(output).toEqual(expected);
});
