package _00290_WordPattern;

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
    @DisplayName("'dog cat cat dog' follows the pattern 'abba'")
    void dog_cat_cat_dog_follows_abba() {
        assertTrue(sol.wordPattern("abba", "dog cat cat dog"));
    }

    @Test
    @DisplayName("'dog cat cat fish' does not follow the pattern 'abba'")
    void dog_cat_cat_fish_does_not_follow_abba() {
        assertFalse(sol.wordPattern("abba", "dog cat cat fish"));
    }

    @Test
    @DisplayName("'dog cat cat dog' does not follows the pattern 'aaaa'")
    void dog_cat_cat_dog_does_not_follow_aaaa() {
        assertFalse(sol.wordPattern("aaaa", "dog cat cat dog"));
    }

    @Test
    @DisplayName("'aa aa aa aa' does not follow the patter 'aaa'")
    void aa_aa_aa_aa_does_not_follow_aaa() {
        assertFalse(sol.wordPattern("aaa", "aa aa aa aa"));
    }

    @Test
    @DisplayName("'dog cat cat' does not follow the patter 'abc'")
    void dog_cat_cat_does_not_follow_abc() {
        assertFalse(sol.wordPattern("abc", "dog cat cat"));
    }

    @Test
    @DisplayName("'dog cat cat' does not follow the patter 'aba'")
    void doc_cat_cat_does_not_follow_aba() {
        assertFalse(sol.wordPattern("aba", "dog cat cat"));
    }

    @Test
    @DisplayName("'happy hacking' follows the pattern 'ab'")
    void happy_hacking_does_not_follow_ab() {
        assertTrue(sol.wordPattern("ab", "happy hacking"));
    }
}
