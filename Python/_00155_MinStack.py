class MinStack:
    """Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.

    Implement the `MinStack` class:
    - `MinStack()` initializes the stack object.
    - `void push(int val)` pushes the element `val` onto the stack.
    - `void pop()` removes the element on the top of the stack.
    - `int top()` gets the top element of the stack.
    - `int getMin()` retrieves the minimum elemenet in the stack.

    You must implement a solution with `O(1)` time complexity for each function.
    """

    def __init__(self):
        """Initialze the stack object.
        """
        self.stack = []

    def push(self, val: int) -> None:
        """Push an element to the top of the stack and keep track of a running
        minimum element.

        Args:
            val (int): the element to add to the stack
        """
        curr_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append([val, curr_min])

    def pop(self) -> None:
        """Remove the top of the stack.
        """
        self.stack.pop()

    def top(self) -> int:
        """Return the value at the top of the stack.

        Returns:
            int: the value at the top of the stack
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Return the minimum value in the stack.

        Returns:
            int: the minimum value in the stack
        """
        return self.stack[-1][1]


import unittest


class Test_MinStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = MinStack()

    def test_example1(self):
        operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
        args = [[], [-2], [0], [-3], [], [], [], []]

        results = []

        for op, val in zip(operations, args):
            if op == "push":
                self.stack.push(val[0])
                results.append(None)
            elif op == "pop":
                self.stack.pop()
                results.append(None)
            elif op == "top":
                results.append(self.stack.top())
            elif op == "getMin":
                results.append(self.stack.getMin())

        self.assertEqual(results, [None, None, None, -3, None, 0, -2])

if __name__ == "__main__":
    unittest.main()