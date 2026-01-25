package _00013_RomanToInteger;

public class Solution {

    /**
     * Given a roman numeral, convert it to an integer.
     * <p>
     * Roman numerals are represented by seven symbols: {@code I}, {@code V},
     * {@code X}, {@code L}, {@code C}, {@code D}, and {@code M}.
     *
     * <pre><code>
     *      Symbols      Value
     *      I            1
     *      V            5
     *      X            10
     *      L            50
     *      C            100
     *      D            500
     *      M            1000
     * </code></pre>
     *
     * There are sex instances where subtraction is used:
     * <ul>
     * <li>{@code I} can be placed before {@code V}(5) and {@code X}(10) to make
     * 4 and 9.</li>
     * <li>{@code X} can be placed before {@code L}(50) and {@code C}(100) to
     * make 40 and 90.</li>
     * <li>{@code C} can be placed before {@code D}(500) and {@code M}(1000) to
     * make 400 and 900.</li>
     * </ul>
     *
     * @param s the roman numeral
     * @return the integer value equivalent to {@code s}
     */
    public int romanToInt(String s) {

        int num = 0;

        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case 'M' ->
                    num += 1000;
                case 'D' ->
                    num += 500;
                case 'C' -> {
                    if (i < s.length() - 1) {
                        switch (s.charAt(i + 1)) {
                            case 'M' -> {
                                num += 900;
                                i++;
                            }
                            case 'D' -> {
                                num += 400;
                                i++;
                            }
                            default ->
                                num += 100;
                        }
                    } else {
                        num += 100;
                    }
                }
                case 'L' ->
                    num += 50;
                case 'X' -> {
                    if (i < s.length() - 1) {
                        switch (s.charAt(i + 1)) {
                            case 'C' -> {
                                num += 90;
                                i++;
                            }
                            case 'L' -> {
                                num += 40;
                                i++;
                            }
                            default ->
                                num += 10;
                        }
                    } else {
                        num += 10;
                    }
                }
                case 'V' ->
                    num += 5;
                case 'I' -> {
                    if (i < s.length() - 1) {
                        switch (s.charAt(i + 1)) {
                            case 'X' -> {
                                num += 9;
                                i++;
                            }
                            case 'V' -> {
                                num += 4;
                                i++;
                            }
                            default ->
                                num += 1;
                        }
                    } else {
                        num += 1;
                    }
                }
                default ->
                    throw new IllegalArgumentException("Invalid Roman numeral.");
            }
        }

        return num;
    }
}
