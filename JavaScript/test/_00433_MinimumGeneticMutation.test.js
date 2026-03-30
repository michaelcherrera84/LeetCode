const minMutation = require("../src/_00433_MinimumGeneticMutation");

test("Example 1", () => {
    const startGene = "AACCGGTT";
    const endGene = "AACCGGTA";
    const bank = ["AACCGGTA"];
    expect(minMutation(startGene, endGene, bank)).toBe(1);
});

test("Example 2", () => {
    const startGene = "AACCGGTT";
    const endGene = "AAACGGTA";
    const bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"];
    expect(minMutation(startGene, endGene, bank)).toBe(2);
});

test("Example 3", () => {
    const startGene = "AACCTTGG";
    const endGene = "AATTCCGG";
    const bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"];
    expect(minMutation(startGene, endGene, bank)).toBe(-1);
});
