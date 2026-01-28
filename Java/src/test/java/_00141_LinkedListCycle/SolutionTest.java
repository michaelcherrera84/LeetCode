package _00141_LinkedListCycle;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

public class SolutionTest {

    private static long totalTime = 0;
    private static int count = 0;

    private long startTime;
    private Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
        startTime = System.currentTimeMillis();
    }

    @AfterEach
    void tearDown() {
        long runtime = System.currentTimeMillis() - startTime;
        if (count != 0) {
            totalTime += runtime;
        }
        System.out.println("Test " + count + ": " + runtime + " ms");
        count++;
    }

    @AfterAll
    static void averageTime() {
        if (count > 1) {
            System.out.println("Average Runtime: " + (totalTime / (count - 1)) + " ms");
        }
    }

    @RepeatedTest(2)
    @DisplayName("1")
    void randomTest1() {
        ListNode head = new ListNode(3);
        head.next = new ListNode(2);
        head.next.next = new ListNode(0);
        head.next.next.next = new ListNode(-1);
        head.next.next.next.next = head.next;
        assertTrue(sol.hasCycle(head));
    }

    @Test
    @DisplayName("2")
    void randomTest2() {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = head;
        assertTrue(sol.hasCycle(head));
    }

    @Test
    @DisplayName("3")
    void list_of_size_one_has_no_cycle() {
        ListNode head = new ListNode(1);
        assertFalse(sol.hasCycle(head));
    }

    @Test
    @DisplayName("4")
    void only_2_nodes_without_cycle() {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        assertFalse(sol.hasCycle(head));
    }
}
