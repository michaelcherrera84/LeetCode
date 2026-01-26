package _00228_SummaryRanges;

import java.util.List;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.contains;
import static org.hamcrest.Matchers.is;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

@SuppressWarnings("unused")
public class SolutionTest {

    private static long totalTime = 0;
    private static int testCount = 0;

    private long startTime = 0;
    private Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
        startTime = System.nanoTime();
    }

    @AfterEach
    void tearDown() {
        long runtime = System.nanoTime() - startTime;
        totalTime += runtime;
        System.out.println("Test " + testCount + ": " + (runtime / 1_000_000.00) + "ms");
        testCount++;
    }

    @AfterAll
    static void reportAverage() {
        System.out.println("Average runtime: " + (totalTime / testCount / 1_000_000.00) + " ms");
    }

    @RepeatedTest(2)
    void random_test_1() {
        assertThat(sol.summaryRanges(new int[] {0, 1, 2, 4, 5, 7}), contains("0->2", "4->5", "7"));
    }

    @Test
    void random_test_2() {
        assertThat(sol.summaryRanges(new int[] {0, 2, 3, 4, 6, 8, 9}), contains("0", "2->4", "6", "8->9"));
    }

    @Test
    void empty_arrary_returns_empty_list() {
        assertThat(sol.summaryRanges(new int[] {}), is(List.of()) );
    }

    @Test
    void min_max_int_values_in_array() {
        assertThat(sol.summaryRanges(new int[] {Integer.MIN_VALUE, Integer.MIN_VALUE + 1, Integer.MAX_VALUE - 1, Integer.MAX_VALUE}), contains("-2147483648->-2147483647", "2147483646->2147483647"));
    }
}
