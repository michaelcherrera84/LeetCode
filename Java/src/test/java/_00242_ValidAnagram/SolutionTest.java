package _00242_ValidAnagram;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
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
    @DisplayName("anagram and nagaram are anagrams")
    void anagram_nagaram() {
        assertTrue(sol.isAnagram("anagram", "nagaram"));
    }

    @Test
    @DisplayName("rat and car are not anagrams")
    void rat_car() {
        assertFalse(sol.isAnagram("rat", "car"));
    }

    @Test
    @DisplayName("strings of unequal length are not anagrams")
    void unequal_length() {
        assertFalse(sol.isAnagram("aa", "aaa"));
    }
}
