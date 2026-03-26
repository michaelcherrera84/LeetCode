from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """You are given an array of variable pairs `equations` and an array of
        real numbers `values`, where `equations[i] = [Aᵢ, Bᵢ]` and `values[i]`
        represent the equation `Aᵢ / Bᵢ = values[i]`. Each `Aᵢ` or `Bᵢ` is a
        string that represents a single variable.

        You are also given some `queries`, where `queries[j] = [Cⱼ, Dⱼ]`
        represents the `jᵗʰ` query where you must find the answer for
        `Cⱼ / Dⱼ = ?`.

        Return *the answers to all queries*. If a single answer cannot be
        determined, return `-1.0`.

        **Note:** The input is always valid. You may assume that evaluating the
        queries will not result in division by zero and that there is no
        contradiction.

        **Note:** The variables that do not occur in the list of equations are
        undefined, so the answer cannot be determined for them.

        Args:
            equations (List[List[str]]): the array of variable pairs
            values (List[float]): values that represent the division of the
            variable pairs
            queries (List[List[str]]): list of new division operations to perform

        Returns:
            List[float]: the result of the new division operations
        """

        graph = defaultdict(dict)
        res = []

        # Build a graph of the given calculations.
        for (var1, var2), val in zip(equations, values):
            graph[var1][var2] = val
            graph[var2][var1] = 1 / val

        def calc(var1, var2, visited):
            """Solve a division equation with the given variables

            Args:
                var1 (str): the dividend variable
                var2 (str): the divisor variable
                visited (set): a set of "visited" variables

            Returns:
                float: the result of the division or -1.0 if we do not have the
                information to perform this division
            """

            # If either variable doesn't exist in the given equations, return -1.0.
            if not graph.get(var1) or not graph.get(var2):
                return -1.0

            # If the divisor is a neighbor of the dividend, then we have the
            # information to perform the division calculation.
            if graph[var1].get(var2):
                return graph[var1][var2]

            # Mark this variable as visited.
            visited.add(var1)
            # For each of the neighbors of the dividend, recursively search for
            # a path to the divisor.
            for var, val in graph[var1].items():
                if var not in visited:
                    res_val = calc(var, var2, visited)
                    # If a path is found to the divisor, return the product of
                    # values along the path.
                    if res_val != -1.0:
                        return val * res_val

            # If a path is not found from the dividend to the divisor, then
            # we do not have enough information to perform the division.
            return -1.0

        # Attempt to perform each calculation in the list of queries.
        for var1, var2 in queries:
            res.append(calc(var1, var2, set()))

        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        actual = self.sol.calcEquation(equations, values, queries)
        self.assertEqual(expected, actual)

    def test_example2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75000, 0.40000, 5.00000, 0.20000]
        actual = self.sol.calcEquation(equations, values, queries)
        self.assertEqual(expected, actual)

    def test_example3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.50000, 2.00000, -1.00000, -1.00000]
        actual = self.sol.calcEquation(equations, values, queries)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
