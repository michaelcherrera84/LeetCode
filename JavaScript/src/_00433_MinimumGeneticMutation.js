/**
 * A gene string can be represented by an 8-character long string, with choices
 * from `'A'`, `'C'`, `'G'`, and `'T'`.
 *
 * Suppose we need to investigate a mutation from a gene string `startGene` to a
 * gene string `endGene` where one mutation is defined as one single character
 * changed in the gene string.
 *
 * - For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.
 *
 * There is also a gene bank `bank` that records all the valid gene mutations. A
 * gene must be in bank to make it a valid gene string.
 *
 * Given the two gene strings `startGene` and `endGene` and the gene bank `bank`,
 * return *the minimum number of mutations needed to mutate from* `startGene`
 * *to* `endGene`. If there is no such a mutation, return `-1`.
 *
 * Note that the starting point is assumed to be valid, so it might not be
 * included in the bank.
 * @param {string} startGene the beginning gene string
 * @param {string} endGene the ending gene string
 * @param {string[]} bank the list of valid mutation
 * @return {number} the minimum number of mutation needed to mutate from
 * `startGene` to `endGene`
 */
var minMutation = function (startGene, endGene, bank) {
    const validSet = new Set(bank); // Use a set for O(1) lookups.

    // We can return right away if the end gene is not valid or the start gene
    // is the same as the end gene.
    if (!validSet.has(endGene)) return -1;
    if (startGene === endGene) return 0;

    /** Queue of validated genes strings to compare to the end gene. */
    const queue = [[startGene, 0]];
    /** Set of alreayd validated and queued gene stings */
    const checked = new Set([startGene]);

    // While there are genes strings to compare to the end gene...
    while (queue.length > 0) {
        // Get the first gene string from the queue along with the number of
        // mutations required to result in this sequence.
        const [currentGene, mutations] = queue.shift();

        // Use an array for easier string mutation.
        const geneArray = currentGene.split("");

        // Check all single gene mutation for validity and add valid mutations 
        // to the queue to compare with the end gene.
        for (let i = 0; i < geneArray.length; i++) {
            // Save the current gene to reset the array.
            const saveGene = geneArray[i];
            for (gene of "ACGT") {
                if (geneArray[i] === gene) continue;

                geneArray[i] = gene;
                const mutation = geneArray.join("");

                // If the mutation is the end gene, count this mutation and
                // return the final result.
                if (mutation === endGene) return mutations + 1;

                // If the mutation is not valid or the mutation as already been
                // queued before, we do not need to add this gene to the queue.
                if (!validSet.has(mutation) || checked.has(mutation)) continue;

                checked.add(mutation);
                queue.push([mutation, mutations + 1]);
            }
            // Reset the gene array for the next mutation.
            geneArray[i] = saveGene;
        }
    }

    return -1;
};

module.exports = minMutation;
