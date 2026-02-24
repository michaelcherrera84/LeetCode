const { canCompleteCircuit, canCompleteCircuit1 } = require("../src/_00134_GasStation");

test("example1", () => {
    const gas = [1, 2, 3, 4, 5];
    const cost = [3, 4, 5, 1, 2];
    expect(canCompleteCircuit(gas, cost)).toBe(3);
});

test("example2", () => {
    const gas = [2, 3, 4];
    const cost = [3, 4, 3];
    expect(canCompleteCircuit(gas, cost)).toBe(-1);
});

test("No trips possible", () => {
    const gas = [1, 1, 1];
    const cost = [2, 2, 2];
    expect(canCompleteCircuit(gas, cost)).toBe(-1);
});

test("One station possible", () => {
    const gas = [2];
    const cost = [1];
    expect(canCompleteCircuit(gas, cost)).toBe(0);
});

test("One station not possible", () => {
    const gas = [1];
    const cost = [2];
    expect(canCompleteCircuit(gas, cost)).toBe(-1);
});

test("[5,1,2,3,4] and [4,4,1,5,1] returns 4", () => {
    const gas = [5, 1, 2, 3, 4];
    const cost = [4, 4, 1, 5, 1];
    expect(canCompleteCircuit(gas, cost)).toBe(4);
});

test("example1-1", () => {
    const gas = [1, 2, 3, 4, 5];
    const cost = [3, 4, 5, 1, 2];
    expect(canCompleteCircuit(gas, cost)).toBe(3);
});

test("example2-1", () => {
    const gas = [2, 3, 4];
    const cost = [3, 4, 3];
    expect(canCompleteCircuit1(gas, cost)).toBe(-1);
});

test("No trips possible - 1", () => {
    const gas = [1, 1, 1];
    const cost = [2, 2, 2];
    expect(canCompleteCircuit1(gas, cost)).toBe(-1);
});

test("One station possible - 1", () => {
    const gas = [2];
    const cost = [1];
    expect(canCompleteCircuit1(gas, cost)).toBe(0);
});

test("One station not possible - 1", () => {
    const gas = [1];
    const cost = [2];
    expect(canCompleteCircuit1(gas, cost)).toBe(-1);
});

test("[5,1,2,3,4] and [4,4,1,5,1] returns 4 - 1", () => {
    const gas = [5, 1, 2, 3, 4];
    const cost = [4, 4, 1, 5, 1];
    expect(canCompleteCircuit1(gas, cost)).toBe(4);
});
