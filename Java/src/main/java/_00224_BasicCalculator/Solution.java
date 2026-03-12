package _00224_BasicCalculator;

import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {
    /**
     * Given a string {@code s} representing a valid expression, implement a basic
     * calculator to evaluate it, and return <i>the result of the evaluation.</i>
     * 
     * <h4>Constraints:</h4>
     * <ul>
     * <li>{@code - 1 <= s.length <= 3 * 10^5}
     * <li>
     * <li>{@code s} consists of digits, {@code '+'}, {@code '-'}, {@code '('},
     * {@code ')'}, and {@code ' '}.</li>
     * <li>{@code s} represents a valid expression.</li>
     * <li>{@code '+'} is <b>not</b> used as a unary operation (i.e., {@code "+1"}
     * and {@code "+(2 + 3)"} is invalid).</li>
     * <li>{@code '-'} could be used as a unary operation (i.e., {@code "-1"} and
     * {@code "-(2 + 3)"} is valid).</li>
     * <li>There will be no two consecutive operators in the input.</li>
     * <li>Every number and running calculation will fit in a signed 32-bit
     * integer.</li>
     * </ul>
     * 
     * @param s the mathematical expression
     * @return the result of the expression
     */
    public int calculate(String s) {

        Deque<Integer> stack = new ArrayDeque<>();
        int total = 0; // current total of sub-expression
        int num = 0; // current number in the expression
        int sign = 1; // current operator or unary operator

        for (char c : s.toCharArray()) {
            // If the character is a digit, build the current number.
            if (Character.isDigit(c))
                num = num * 10 + (c - '0');
            
            // If the character is a '+' pr '-', perform the current operation,
            // store the new sign/op, and reset num.
            else if (c == '+' || c == '-') {
                total += num * sign;
                sign = c == '+' ? 1 : -1;
                num = 0;
            } 
            
            // If the character is '(', add the current total and sign to the
            // stack, and start a new sub-expression.
            else if (c == '(') {
                stack.push(total);
                stack.push(sign);
                total = 0;
                sign = 1;
            } 
            
            // If the character is ')', perform the current operation. Then, add
            // this value to the previous total on the stack.
            else if (c == ')') {
                total += num * sign;
                int prev_sign = stack.pop();
                int prev_total = stack.pop();
                total = prev_total + prev_sign * total;
                num = 0;
            }
        }

        // If the last character was a number, perform the final operations.
        return total + num * sign;
    }
}
