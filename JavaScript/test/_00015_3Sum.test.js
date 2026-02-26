const threeSum = require("../src/_00015_3Sum");

/**
 * Sort a 2d array of numbers.
 * @param {number[][]} arr the array
 * @returns the sorted array
 */
function sort(arr) {
    arr.map((subArr) => {
        [...subArr].sort();
    }).sort((a, b) => {
        a.join(",") < b.join(",") ? -1 : 1;
    });

    return arr;
}

test("Example 1", () => {
    const nums = [-1, 0, 1, 2, -1, -4];
    const expected = [
        [-1, -1, 2],
        [-1, 0, 1],
    ];
    const actual = threeSum(nums);

    expect(sort(actual)).toEqual(sort(expected));
});

test("Example 2", () => {
    const nums = [0, 1, 1];
    const expected = [];
    const actual = threeSum(nums);

    expect(sort(actual)).toEqual(sort(expected));
});

test("Example 2", () => {
    const nums = [0, 0, 0];
    const expected = [[0, 0, 0]];
    const actual = threeSum(nums);

    expect(sort(actual)).toEqual(sort(expected));
});

test("[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]", () => {
    const nums = [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10];
    const expected = [
        [-10, 5, 5],
        [-5, 0, 5],
        [-4, 2, 2],
        [-3, -2, 5],
        [-3, 1, 2],
        [-2, 0, 2],
    ];
    const actual = threeSum(nums);

    expect(sort(actual)).toEqual(sort(expected));
});
