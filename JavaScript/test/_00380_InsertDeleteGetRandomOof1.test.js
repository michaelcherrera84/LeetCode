const RandomizedSet = require("../src/_00380_InsertDeleteGetRandomOof1");

test("example1", () => {
    const rs = new RandomizedSet();

    expect(rs.insert(1)).toBe(true);
    expect(rs.remove(2)).toBe(false);
    expect(rs.insert(2)).toBe(true);

    const random1 = rs.getRandom();
    expect([1, 2]).toContain(random1);

    expect(rs.remove(1)).toBe(true);
    expect(rs.insert(2)).toBe(false);

    const random2 = rs.getRandom();
    expect(random2).toBe(2);
});
