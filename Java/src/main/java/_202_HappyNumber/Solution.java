package _202_HappyNumber;

import java.util.HashSet;
import java.util.Set;

public class Solution {

    /**
     * Given a number {@code n}, return {@code true} <i>if</i> {@code n} <i>is a
     * happy number, and</i> {@code false} <i>if not</i>.
     * <p>
     * A <b>happy number</b> is a number defined by the following process:
     * <ul>
     * <li>Starting with any positive integer, replace the number by the sum of
     * the squares of its digits.</li>
     * <li>Repeat the process until number equal 1, or it <b>loops endlessly in
     * a cycle</b> which does not include 1.</li>
     * <li>Those numbers for which this process <b>ends in 1</b> are happy.</li>
     * </ul>
     *
     * @param n the number
     * @return {@code true} if {@code n} is a happy number, or {@code false}
     * otherwise
     */
    public boolean isHappy(int n) {

        int slow = n;                   // will hold the next sum of squares.
        int fast = sumOfSquares(n);     // will hold every other sum of squares.

        // Detect the cycle. Either fast will hit 1 (the number is happy), or 
        // fast and slow will hit the same sum (the number is not happy).
        while (fast != 1 && fast != slow) {
            slow = sumOfSquares(slow);
            fast = sumOfSquares(sumOfSquares(fast));
        }

        return fast == 1;
    }

    /**
     * Given a number {@code n}, return {@code true} <i>if</i> {@code n} <i>is a
     * happy number, and</i> {@code false} <i>if not</i>.
     * <p>
     * A <b>happy number</b> is a number defined by the following process:
     * <ul>
     * <li>Starting with any positive integer, replace the number by the sum of
     * the squares of its digits.</li>
     * <li>Repeat the process until number equal 1, or it <b>loops endlessly in
     * a cycle</b> which does not include 1.</li>
     * <li>Those numbers for which this process <b>ends in 1</b> are happy.</li>
     * </ul>
     *
     * @param n the number
     * @return {@code true} if {@code n} is a happy number, or {@code false}
     * otherwise
     */
    public boolean isHappy1(int n) {
        Set<Integer> sums = new HashSet<>();  // to keep track of sums of squares

        // Replace `n` with the sum of the squares of its digits until `n` 
        // becomes 1 or until a sum repeats itself.
        while (n != 1 && !sums.contains(n)) {
            sums.add(n);
            n = sumOfSquares(n);
        }

        return n == 1;
    }

    /**
     * Calculate the sum of the squares of the digits in a number {@code n}.
     *
     * @param n the number
     * @return the sum of the squares of the digits in {@code n}
     */
    private int sumOfSquares(int n) {
        int sum = 0;

        // While there are still digits in n...
        while (n > 0) {
            int digit = n % 10;     // the ones place of n
            sum += digit * digit;   // Add the square of the digit to the sum.
            n /= 10;                // Truncate the ones digit of n.
        }
        return sum;
    }
}
