from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """You are given an array of strings `tokens` that represents an 
        arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return *an integer that represents the value
        of the expression*.

        **Note** that:
        - The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
        - Each operand may be an integer or another expression.
        - The division between two integers always **truncates toward zero**.
        - There will not be any division by zero.
        - The input represents a valid arithmetic expression in a reverse polish
        notation.
        - The answer and all the intermediate calculations can be represented in
        a **32-bit** integer.

        Args:
            tokens (List[str]): the array of tokens

        Returns:
            int: an integer that represents the value of the expression
        """

        ops = []

        # For each token (operand/operation) in tokens, if the token is an 
        # operation, perform the operation on the last two operands in in ops,
        # add the result to ops, and remove the oparands used. Otherwise, add
        # an operand to ops.
        for op in tokens:
            match op:
                case "+":
                    b = ops.pop()
                    a = ops.pop()
                    ops.append(a + b)
                case "-":
                    b = ops.pop()
                    a = ops.pop()
                    ops.append(a - b)
                case "*":
                    b = ops.pop()
                    a = ops.pop()
                    ops.append(a * b)
                case "/":
                    b = ops.pop()
                    a = ops.pop()
                    ops.append(int(a / b))
                case _:
                    ops.append(int(op)) 

        return ops[-1]


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        actual = self.sol.evalRPN(tokens)
        self.assertEqual(expected, actual)

    def test_example2(self):
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6
        actual = self.sol.evalRPN(tokens)
        self.assertEqual(expected, actual)

    def test_example3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22
        actual = self.sol.evalRPN(tokens)
        self.assertEqual(expected, actual)

    def test_negative_division(self):
        tokens = ["1", "-6", "+", "5", "-", "3", "/"]
        expected = -3
        actual = self.sol.evalRPN(tokens)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
