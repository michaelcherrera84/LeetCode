class Solution:
    def calculate(self, s: str) -> int:
        """Given a string `s` representing a valid expression, implement a basic 
        calculator to evaluate it, and return *the result of the evaluation*.

        Constraints:
        - `1 <= s.length <= 3 * 10^5`
        - `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
        - `s` represents a valid expression.
        - `'+'` is **not** used as a unary operation (i.e., `"+1"` and 
        `"+(2 + 3)"` is invalid).
        - `'-'` could be used as a unary operation (i.e., `"-1"` and 
        `"-(2 + 3)"` is valid).
        - There will be no two consecutive operators in the input.
        - Every number and running calculation will fit in a signed 32-bit 
        integer.

        Args:
            s (str): the mathematical expression

        Returns:
            int: the result of the expression
        """

        n = len(s)
        stack = []  # inner expression totals
        total = 0  # running total
        sign = 1  # current sign of operation ('+' -> 1, '-' -> -1)

        i = 0
        while i < n:
            # If the character is a digit, build the number one place at a time.
            if s[i].isdigit():
                x = 0
                while i < n and s[i].isdigit():
                    x = x * 10 + int(s[i])
                    i += 1
                total += x * sign
                continue
            
            elif s[i] == "+":
                sign = 1
            
            elif s[i] == "-":
                sign = -1

            # If the character is '(' start a new inner expression. Store the
            # current total and the current sign in the stack.
            elif s[i] == "(":
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1

            # If the character is ')', combine the total of this inner
            # inner expression with the previous total.
            elif s[i] == ")":
                prev_sign = stack.pop()
                prev_total = stack.pop()
                total = prev_total + prev_sign * total

            i += 1

        return total

import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        s = "1 + 1"
        expected = 2
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)

    def test_example2(self):
        s = " 2-1 + 2 "
        expected = 3
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)

    def test_example3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)

    def test_negative_num(self):
        s = "-1 - 1"
        expected = -2
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)

    def test_negative_paren(self):
        s = "-(1 + 1)"
        expected = -2
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)

    def test_nagative_in_paren(self):
        s = "1-(     -2)"
        expected = 3
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)

    def test_nagative_paren_nagative_in_paren(self):
        s = "-(-2-3)-3"
        expected = 2
        actual = self.sol.calculate(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
