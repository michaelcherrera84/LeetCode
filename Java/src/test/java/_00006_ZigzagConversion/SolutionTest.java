package _00006_ZigzagConversion;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

@SuppressWarnings("unused")
public class SolutionTest {

    private Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
    }

    @Test
    void example1() {
        assertEquals("PAHNAPLSIIGYIR", sol.convert("PAYPALISHIRING", 3));
    }

    @Test
    void example2() {
        assertEquals("PINALSIGYAHRPI", sol.convert("PAYPALISHIRING", 4));
    }
}
