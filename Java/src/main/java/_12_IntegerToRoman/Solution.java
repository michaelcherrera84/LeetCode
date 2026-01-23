package _12_IntegerToRoman;

public class Solution {

    /**
     * Given an integer, convert it to a Roman numeral.
     * <p>
     * Roman numberal are formed by appending the conversions of decimal place
     * values from highest to lowest. Converting a decimal place value into a
     * Roman numaral has the following rules:
     * <ul>
     * <li>If the value does not start with 4 or 9, select the symbol of the
     * maximal value that can be subtracted from the input, append that symbol
     * to the result, subtract its value, and convert the remainder to a Roman
     * numeral.</li>
     * <li>If the value starts with 4 or 9 use the <b>subtractive form</b>
     * representing one symbol subtracted from the following symbol, for
     * example, 4 is 1 ({@code I}) less than 5 ({@code V}): IV and 9 is 1
     * ({@code I}) less than 10 ({@code X}): {@code IX}. Only the following
     * subtractive forms are used: 4 ({@code IV}), 9 ({@code IX}), 40
     * ({@code XL}), 90 ({@code XC}), 400 ({@code CD}) and 900 ({@code CM})</li>
     * <li>Only powers of 10 ({@code I}, {@code X}, {@code C}, {@code M}) can be
     * appended consecutively at most 3 times to represent multiples of 10. You
     * cannot append 5 ({@code V}), 50 ({@code L}), or 500 ({@code D}) multiple
     * times. If you need to append a symbol 4 times use the <b>subtractive
     * form</b>.</li>
     * </ul>
     *
     * @param num the integer to convert
     * @return the Roman numeral equivalent to {@code num}
     */
    public String intToRoman(int num) {

        String romanNumeral = "";

        int i = 0;
        while (num > 0) {
            int val = num % 10;
            int place = (int) Math.pow(10, i++);

            switch (place) {
                case 1 -> {
                    if (val == 9) {
                        romanNumeral = "IX";
                    } else if (val >= 5) {
                        romanNumeral = "V";
                        for (int j = 0; j < val - 5; j++) {
                            romanNumeral += "I";
                        }
                    } else if (val == 4) {
                        romanNumeral = "IV";
                    } else {
                        for (int j = 0; j < val; j++) {
                            romanNumeral += "I";
                        }
                    }
                }
                case 10 -> {
                    if (val == 9) {
                        romanNumeral = "XC" + romanNumeral;
                    } else if (val >= 5) {
                        String n = "L";
                        for (int j = 0; j < val - 5; j++) {
                            n += "X";
                        }
                        romanNumeral = n + romanNumeral;
                    } else if (val == 4) {
                        romanNumeral = "XL" + romanNumeral;
                    } else {
                        for (int j = 0; j < val; j++) {
                            romanNumeral = "X" + romanNumeral;
                        }
                    }
                }
                case 100 -> {
                    if (val == 9) {
                        romanNumeral = "CM" + romanNumeral;
                    } else if (val >= 5) {
                        String n = "D";
                        for (int j = 0; j < val - 5; j++) {
                            n += "C";
                        }
                        romanNumeral = n + romanNumeral;
                    } else if (val == 4) {
                        romanNumeral = "CD" + romanNumeral;
                    } else {
                        for (int j = 0; j < val; j++) {
                            romanNumeral = "C" + romanNumeral;
                        }
                    }
                }
                case 1000 -> {
                    for (int j = 0; j < val; j++) {
                        romanNumeral = "M" + romanNumeral;
                    }
                }
                default ->
                    throw new IllegalArgumentException("Input must be between 1 and 3999");
            }

            num = num / 10;
        }

        return romanNumeral;
    }

    /**
     * Given an integer, convert it to a Roman numeral.
     * <p>
     * Roman numberal are formed by appending the conversions of decimal place
     * values from highest to lowest. Converting a decimal place value into a
     * Roman numaral has the following rules:
     * <ul>
     * <li>If the value does not start with 4 or 9, select the symbol of the
     * maximal value that can be subtracted from the input, append that symbol
     * to the result, subtract its value, and convert the remainder to a Roman
     * numeral.</li>
     * <li>If the value starts with 4 or 9 use the <b>subtractive form</b>
     * representing one symbol subtracted from the following symbol, for
     * example, 4 is 1 ({@code I}) less than 5 ({@code V}): IV and 9 is 1
     * ({@code I}) less than 10 ({@code X}): {@code IX}. Only the following
     * subtractive forms are used: 4 ({@code IV}), 9 ({@code IX}), 40
     * ({@code XL}), 90 ({@code XC}), 400 ({@code CD}) and 900 ({@code CM})</li>
     * <li>Only powers of 10 ({@code I}, {@code X}, {@code C}, {@code M}) can be
     * appended consecutively at most 3 times to represent multiples of 10. You
     * cannot append 5 ({@code V}), 50 ({@code L}), or 500 ({@code D}) multiple
     * times. If you need to append a symbol 4 times use the <b>subtractive
     * form</b>.</li>
     * </ul>
     *
     * @param num the integer to convert
     * @return the Roman numeral equivalent to {@code num}
     */
    public String intToRoman1(int num) {

        if (num < 1 || num > 3999) {
            throw new IllegalArgumentException("Input value must be between 1 and 3999.");
        }

        // integer values for each Roman numeral
        int[] values = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        // Roman numerals
        String[] numerals = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder romanNumeral = new StringBuilder();   // the result

        // Traverse each integer value.
        for (int i = 0; i < values.length; i++) {

            // If num is greater than or equal to the current integer value,
            // add the appropriate Roman numeral to the result, subtact the
            // value from num, and then compare num to that value again.
            if (num >= values[i]) {
                romanNumeral.append(numerals[i]);
                num -= values[i--];
            }
        }

        return romanNumeral.toString();
    }
}
