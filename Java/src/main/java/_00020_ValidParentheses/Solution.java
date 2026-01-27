package _00020_ValidParentheses;

import java.util.Stack;

public class Solution {

    /**
     * Given a string {@code s} containing just the characters
     * {@code '('}, {@code ')'}, <code>'{'</code>, <code>'}'</code>,
     * {@code '['}, and {@code ']'}, determine if the input string is valid.
     * <p>
     * An input string is valid if:
     * <ol>
     * <li>Open brackets must be closed by the same type of brackets.</li>
     * <li>Open brackets must be closed in the correct order.</li>
     * <li>Every close bracket has a corresponding open bracket of the same
     * type.</li>
     * </ol>
     *
     * @param s string of brackets
     * @return {@code true} is {@code s} is valid, or {@code false} otherwise.
     */
    public boolean isValid(String s) {

        if (s == null || s.length() < 2) {
            return false;
        }

        // holds the expected closing braces
        Stack<Character> closingBrackets = new Stack<>();

        // For each letter in `s`, if the letter is an openining bracket, add 
        // the corresponding closing bracket to the stack. If the letter is a 
        // closing braket, it must match the last braket added to the stack.
        // Otherwise, the string is invalid.
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case '(' ->
                    closingBrackets.push(')');
                case '{' ->
                    closingBrackets.push('}');
                case '[' ->
                    closingBrackets.push(']');
                case ')' -> {
                    if (closingBrackets.empty() || closingBrackets.pop() != ')') {
                        return false;
                    }
                }
                case '}' -> {
                    if (closingBrackets.empty() || closingBrackets.pop() != '}') {
                        return false;
                    }
                }
                case ']' -> {
                    if (closingBrackets.empty() || closingBrackets.pop() != ']') {
                        return false;
                    }
                }
                default -> {
                    return false;
                }
            }
        }

        // If the string is not found to be invalid in the loop, and all closing 
        // brackets from the stack have been used then the string is valid.
        return closingBrackets.isEmpty();
    }
}
