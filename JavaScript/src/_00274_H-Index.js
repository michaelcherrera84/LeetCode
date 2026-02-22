/**
 * Given an array of integers `citations` where `citations[i]` is the number of
 * citations a researcher received for their `ith` paper, return *the
 * researcher's h-index.*
 *
 * The h-index is defined as the maximum value of `h` such that the given
 * researcher has published at least `h` papers that have each been cited at
 * least `h` times.
 *
 * @param {number[]} citations the number of citations a researcher received for
 * their `ith` paper
 * @returns {number} the researcher's h-index
 */
var hIndex = function (citations) {
    // Each index represents a citation count, up to the total number of papers,
    // and the value is the number of papers with at least that many citations.
    let paperCounts = new Array(citations.length + 1).fill(0);

    // For each element in citations...
    citations.forEach((count) => {
        // If the citation count is greater than or equal to the number of
        // papers, then increment the paper count of the max citation count.
        if (count >= citations.length) paperCounts[citations.length]++;
        // Otherwise, increment the paper count for this citation count.
        else paperCounts[count]++;
    });

    let papersTotal = 0; // running sum of papers for each citation count.

    // For each paper count starting with the max citation count...
    for (let i = paperCounts.length - 1; i >= 0; i--) {
        // Add this paper count to the sum of papers.
        papersTotal += paperCounts[i];

        // If the sum of papers is greater than or equal to the current 
        // citation count, then this citation count is the H-index.
        if (papersTotal >= i) return i;
    }

    return 0;
};

module.exports = { hIndex };
