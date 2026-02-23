/**
 * Initialize the `RandomizedSet` object.
 */
var RandomizedSet = function () {
    this.map = new Map(); // map of values and their indices in the list
    this.list = []; // list of values in this set
};

/**
 * Insert an item `val` in the set if not present. Return `true` if the item was
 * not present, or `false` otherwise
 * @param {number} val item to insert into the set
 * @return {boolean} `true` if the item was not present, or `false` otherwise
 */
RandomizedSet.prototype.insert = function (val) {
    if (this.map.has(val)) return false;
    this.map.set(val, this.list.push(val) - 1);
    return true;
};

/**
 * Remove an item `val` from the set if present. Return `true` if the item was
 * present, or `false` otherwise.
 * @param {number} val the item to remove from the set
 * @return {boolean} `true` if the item was present, or `false` otherwise
 */
RandomizedSet.prototype.remove = function (val) {
    if (!this.map.has(val)) return false;

    const last = this.list[this.list.length - 1]; // last value in the list
    const iOfVal = this.map.get(val); // index of the value to be removed

    // Overwrite the value to be removed with the last value.
    this.list[iOfVal] = last;
    // Set the new index of the value that was moved.
    this.map.set(last, iOfVal);

    this.list.pop(); // Remove the end of the list.
    this.map.delete(val); // Remove the value to remove from the map.

    return true;
};

/**
 * Return a random element from the current set of elements.
 * @return {number} a random element from the current set of elements
 */
RandomizedSet.prototype.getRandom = function () {
    const rand = Math.floor(Math.random() * this.list.length);
    return this.list[rand];
};

module.exports = RandomizedSet;
