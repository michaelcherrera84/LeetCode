/** Definition for singly-linked list. */
function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * Given the `head` of a linked list, return *the list after sorting it in
 * **ascending order***.
 *
 * @param {ListNode} head the head of a singly-linked list
 * @return {ListNode} the list sorted
 */
var sortList = function (head) {
    /** Get the size of the linked list. */
    function size(node) {
        let size = 0;
        while (node) {
            size++;
            node = node.next;
        }
        return size;
    }

    /**
     * Separates a section of size `n` from the front of the list beginning at
     * the provided `node`.
     *
     * @param {ListNode} node node in a linked list
     * @param {number} n section size
     * @returns the node after the section
     */
    function split(node, n) {
        let prev = null;
        while (node && n > 0) {
            prev = node;
            node = node.next;
            n--;
        }

        if (prev) prev.next = null;

        return node;
    }

    /**
     * Append each node of from two sections of a linked list to the provided
     * `node` in order, and return the end of the sorted section.
     *
     * @param {ListNode} l a section of a linked list
     * @param {ListNode} r a section of a linked list
     * @param {ListNode} node the node that the sorted sections will be appended to.
     * @returns the end of this sorted section
     */
    function merge(l, r, node) {
        while (l && r) {
            if (l.val < r.val) {
                node.next = l;
                l = l.next;
            } else {
                node.next = r;
                r = r.next;
            }

            node = node.next;
        }

        node.next = l ? l : r;

        while (node.next) node = node.next;

        return node;
    }

    const dummy = new ListNode(0, head);
    const n = size(head); // size of the linked list
    let i = 1; // size of list sections to be sorted

    // While the sections are smaller than the entire list, split the list into
    // sections that double in size each iterations, sort the sections, and
    // recombine the sections.
    while (i < n) {
        let prev = dummy,
            curr = dummy.next;

        while (curr) {
            let left = curr;
            let right = split(left, i);
            curr = split(right, i);
            prev = merge(left, right, prev);
        }

        i *= 2;
    }

    return dummy.next;
};

module.exports = { ListNode, sortList };
