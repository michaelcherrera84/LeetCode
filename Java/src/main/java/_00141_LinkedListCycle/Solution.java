package _00141_LinkedListCycle;

@SuppressWarnings("unused")
class ListNode {

    int val;
    ListNode next;

    public ListNode(int x) {
        val = x;
        next = null;
    }

}

public class Solution {

    /**
     * Given {@code head}, the head of a linked list, determine if the linked
     * list has a cycle in it.
     * <p>
     * There is a cycle in a linked list if there is some node in the list that
     * can be reached again by continuously following the the {@code next}
     * pointer. Internally, {@code pos} is used to denote the index of the node
     * that tail's {@code next} pointer is connected to. <b>Note that</b>
     * {@code pos} <b> is not passed as a parameter</b>.
     *
     * @param head the head of linked list
     * @return {@code true} if there is a cycle in the linked list. Otherwise,
     * return {@code false}
     */
    boolean hasCycle(ListNode head) {

        if (head == null || head.next == null) {
            return false;
        }

        ListNode slow = head;       // to advance 1 node at a time
        ListNode fast = head.next;  // to advance 2 nodes at a time

        // If fast is ever null, or there is no node after fast, we've reach the 
        // end of the list and there is no cycle.
        while (fast != null && fast.next != null) {
            
            slow = slow.next;       // Advance 1 node.
            fast = fast.next.next;  // Advance 2 nodes.

            // If slow is equal to fast, there must be a cycle.
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}
