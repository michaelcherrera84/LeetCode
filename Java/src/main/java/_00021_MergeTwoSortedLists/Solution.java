package _00021_MergeTwoSortedLists;

class ListNode {

    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

}

public class Solution {

    /**
     * Given the heads of two sorted linked lists {@code list1} and
     * {@code list2}, merge the two lists into one <b>sorted</b> list. The list
     * should be made by splicing together the nodes of the first two lists.
     *
     * @param list1 the head of the first sorted linked list
     * @param list2 the head of the second sorted linked list
     * @return the head of the merged linked list
     */
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if (list1 == null && list2 == null) {
            return null;
        }
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        // dummy will be the node before the head of the merged list.
        ListNode dummy = new ListNode();
        ListNode tail = dummy;  // pointer for the merged list.

        // While list1 or list2 has nodes...
        while (list1 != null && list2 != null) {

            // If current value list1 is less than or equal to the current value 
            // of list2, then the next node of the merged list is the current 
            // node of list1. Advance the list1 pointer.
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                // Otherwise, the current node of list2 is the next node of the 
                // merged list. Advance the list2 pointer.
                tail.next = list2;
                list2 = list2.next;
            }

            // Advance the merged list pointer.
            tail = tail.next;
        }

        // If list1 has nodes, append the remaining list1 to the merged list. 
        // Otherwise, append the remaining list2 to the merged list.
        tail.next = list1 != null ? list1 : list2;

        return dummy.next;
    }
}
