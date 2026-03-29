from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        A gene string can be represented by an 8-character long string, with
        choices from `'A'`, `'C'`, `'G'`, and `'T'`.

        Suppose we need to investigate a mutation from a gene string `startGene`
        to a gene string `endGene` where one mutation is defined as one single
        character changed in the gene string.

        - For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

        There is also a gene bank `bank` that records all the valid gene
        mutations. A gene must be in `bank` to make it a valid gene string.

        Given the two gene strings `startGene` and `endGene` and the gene bank
        `bank`, return *the minimum number of mutations needed to mutate from*
        `startGene` *to* `endGene`. If there is no such a mutation, return `-1`.

        Note that the starting point is assumed to be valid, so it might not be
        included in the bank.

        Args:
            startGene (str): beginning 8-character gene string
            endGene (str): ending 8-character gene string
            bank (List[str]): list of valid gene mutation

        Returns:
            int: the minimum number of mutations needed to mutate from
            `startGene` to `endGene`
        """

        bank_set = set(bank) # Use set for O(1) lookups.

        # If the startGene is not the endGene and the endGene is not in the bank,
        # we know right away that there is no valid mutation path to the endGene.
        if startGene != endGene and endGene not in bank_set:
            return -1

        # queue of valid gene strings to check against the endGene and the 
        # number of mutataions required to get to each gene string
        queue = deque([(startGene, 0)])
        # set of already validated genes that will not need to be queued again
        checked = {startGene}

        # While there are valid gene strings to check against the endGene
        while queue:
            # Get the first gene string in the queue and the number of mutations
            # required to get to this gene string.
            gene_string, mutations = queue.popleft()

            # If this gene string is the endGene, we can return the mutations count.
            if gene_string == endGene:
                return mutations

            # For each gene in the gene string, try each of the other genes in 
            # this position and check for validity.
            for i in range(len(gene_string)):
                for gene in "ACGT":
                    if gene_string[i] != gene:
                        mutation = gene_string[:i] + gene + gene_string[i + 1 :]
                        
                        # If this is a valid mutation and this mutation hasn't
                        # been encountered yet add it to the queue to check 
                        # against the endGene and add it to the set of gene
                        # strings checked for validity. 
                        if mutation in bank_set and mutation not in checked:
                            checked.add(mutation)
                            queue.append((mutation, mutations + 1))
        
        # If no valid chain of mutations was found, return -1.
        return -1


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        actual = self.sol.minMutation(startGene, endGene, bank)
        self.assertEqual(expected, actual)

    def test_example2(self):
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        actual = self.sol.minMutation(startGene, endGene, bank)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
