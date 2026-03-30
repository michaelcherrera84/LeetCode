import Cocoa
import Testing

class Solution {
    /// Given the two gene strings `startGene` and `endGene` and the gene bank
    /// `bank`, return *the minimum number of mutations needed to mutate from*
    /// `startGene` *to* `endGene`. If there is no such a mutation, return `-1`.
    ///
    /// A gene string can be represented by an 8-character long string, with
    /// choices from `'A'`,` 'C'`,` 'G'`, and` 'T'`.
    ///
    /// Suppose we need to investigate a mutation from a gene string `startGene`
    /// to a gene string `endGene` where one mutation is defined as one single
    /// character changed in the gene string.
    ///
    /// - For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.
    ///
    /// There is also a gene bank `bank` that records all the valid gene
    /// mutations. A gene must be in `bank` to make it a valid gene string.
    ///
    /// Note that the starting point is assumed to be valid, so it might not be
    /// included in the bank.
    ///
    /// - Parameters:
    ///   - startGene: beginning gene string
    ///   - endGene: ending gene string
    ///   - bank: list of valid mutations
    /// - Returns: the minimum number of mutations needed to mutate from
    /// `startGene` to `endGene`
    func minMutation(_ startGene: String, _ endGene: String, _ bank: [String])
        -> Int
    {
        let geneSet = Set(bank)  // use a set for O(1) lookups

        // If the endGene is not valid we can return right away.
        if !geneSet.contains(endGene) { return -1 }
        // If the startGene and the endGene are the same, no mutations are needed.
        if startGene == endGene { return 0 }

        /** Queue of valid genes to check against the ending gene. */
        var queue: [(String, Int)] = [(startGene, 0)]
        /** Set of genes that have already been checked for validity and added
         to the queue. */
        var checked: Set<String> = [startGene]

        // While there are still gene strings to compare to the end gene...
        while !queue.isEmpty {
            // Get the first gene string from the queue with the number of
            // mutations required to get to this particular gene string.
            let (currentGene, mutations) = queue.removeFirst()
            // Use an array for easier character manipulation.
            var geneArray = Array(currentGene)

            // Check each gene for valid mutations
            for i in 0..<geneArray.count {
                let originalGene = geneArray[i]

                for gene in "ACGT" {
                    guard gene != originalGene else { continue }

                    geneArray[i] = gene
                    let mutation = String(geneArray)

                    // If the mutation is the endGene, count this mutation and
                    // return the total count of required mutations.
                    if mutation == endGene { return mutations + 1 }

                    // If we've already validated this gene string and added it
                    // to the queue, we don't need to do it again. We also do
                    // not add this mutation to the queue if it is not valid.
                    guard !checked.contains(mutation),
                        geneSet.contains(mutation)
                    else {
                        continue
                    }

                    checked.insert(mutation)
                    queue.append((mutation, mutations + 1))
                }

                // Reset the geneArray for the next mutation.
                geneArray[i] = originalGene
            }
        }

        return -1
    }
}

let sol = Solution()
sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
