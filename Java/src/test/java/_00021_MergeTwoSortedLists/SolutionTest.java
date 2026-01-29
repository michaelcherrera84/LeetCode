package _00021_MergeTwoSortedLists;

import java.util.Arrays;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

@SuppressWarnings("unused")
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
        ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        int[] resultCheck = new int[] {1, 1, 2, 3, 4, 4};

        ListNode result = sol.mergeTwoLists(list1, list2);
        
        for (int i = 0; i < resultCheck.length; i++) {
            assertEquals(result.val, resultCheck[i]);
            result = result.next;
        }
    }

    @Test
    @DisplayName("2")
    void two_empty_lists_returns_null() {
        assertNull(sol.mergeTwoLists(null, null));
    }

    @Test
    @DisplayName("3")
    void one_empty_list_returns_the_other_list() {
        ListNode list1 = new ListNode();
        int[] resultCheck = new int[] {0};

        ListNode result = sol.mergeTwoLists(list1, null);

        for (int i = 0; i < resultCheck.length; i++) {
            assertEquals(result.val, resultCheck[i]);
            result = result.next;
        }
    }

    @RepeatedTest(5)
    @DisplayName("4")
    void completely_random_test() {
        int size = (int) (Math.random() * 100) + 1;
        int[] resultCheck = new int[size];

        ListNode list1 = new ListNode();
        ListNode list2 = new ListNode();

        for (int i = 0; i < resultCheck.length; i++) {
            resultCheck[i] = (int) (Math.random() * 200) - 100;
        }

        Arrays.sort(resultCheck);

        ListNode p1 = list1;
        ListNode p2 = list2;
        for (int i = 0; i < resultCheck.length; i++) {
            int random = (int) (Math.random() * 2);
            if (random == 0) {
                p1.next = new ListNode();
                p1 = p1.next;
                p1.val = resultCheck[i];
            } else {
                p2.next = new ListNode();
                p2 = p2.next;
                p2.val = resultCheck[i];
            }
        }

        ListNode result = sol.mergeTwoLists(list1.next, list2.next);

        for (int i = 0; i < resultCheck.length; i++) {
            assertEquals(result.val, resultCheck[i]);
            result = result.next;
        }
    }
}
