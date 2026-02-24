/**
 * There are `n` gas stations along a circular route, where the aound of gas at
 * the `ith` station is `gas[i]`.
 *
 * You have a car with an unlimited gas tank and it costs `cost[i]` of gas to
 * travel from the `ith` station to its next `(i + 1)th` station. You begin the
 * journey with an empty tank at one of the gas stations.
 *
 * Given two integer arrays `gas` and `cost`, return *the starting gas station's
 * index if you can travel around the circuit once in the clockwise direction,
 * otherwise return* `-1`.
 * @param {number[]} gas the gas stations with an amount of gas at each
 * @param {number[]} cost the cost (in gas) to travel to the next station
 * @return {number} the gas station from which you can make a round trip, or
 * `-1` if no round trip is possible
 */
var canCompleteCircuit = function (gas, cost) {
    const n = gas.length;

    // If there is only one gas station, can we circle it or not?
    if (n === 1) {
        if (gas[0] >= cost[0]) return 0;
        return -1;
    }

    let start = 0; // possible starting station
    let tank = 0; // gas in tank
    let curr = 0; // current station where we are
    let next = 1; // the next station we're trying to get to

    // Travel until we make a round trip or determind the trip isn't possible.
    while (true) {
        // If we can get enough gas at this station to make to the next station
        // then make the trip.
        if (tank + gas[curr] >= cost[curr]) {
            tank = tank + gas[curr] - cost[curr]; // gas remaining after trip.
            // Next is now the station we just traveled to. If it is the station
            // we started at, then we've made a round trip.
            if (next === start) return start;
        } else {
            // If there wasn't enough gas at the current station, then we can
            // try starting at the next station, but if the next station is
            // behind us, then the round trip is not possible.
            if (next <= start) return -1;
            else start = next;
            tank = 0; // Reset tank if previous start failed.
        }
        curr = next; // We are now at the old `next` station.
        // The new `next` station could be the first if we are at the last station.
        next = next + 1 < n ? next + 1 : 0;
    }
};

/**
 * There are `n` gas stations along a circular route, where the aound of gas at
 * the `ith` station is `gas[i]`.
 *
 * You have a car with an unlimited gas tank and it costs `cost[i]` of gas to
 * travel from the `ith` station to its next `(i + 1)th` station. You begin the
 * journey with an empty tank at one of the gas stations.
 *
 * Given two integer arrays `gas` and `cost`, return *the starting gas station's
 * index if you can travel around the circuit once in the clockwise direction,
 * otherwise return* `-1`.
 * @param {number[]} gas the gas stations with an amount of gas at each
 * @param {number[]} cost the cost (in gas) to travel to the next station
 * @return {number} the gas station from which you can make a round trip, or
 * `-1` if no round trip is possible
 */
var canCompleteCircuit1 = function (gas, cost) {
    let total = 0;  // running net total of gas
    let tank = 0;   // running amount of gas in tank
    let start = 0;  // possible starting station

    // Determine net gas from each station, and consider possible starting stations.
    for (let curr = 0; curr < gas.length; curr++) {
        // The net gas is the amount at the station minus the amount needed to
        // travel to the next station.
        const net = gas[curr] - cost[curr];

        total += net;   // Add the net to the total net.
        tank += net;    // Update the amount in the tank.

        // If we ran out of gas, try a new starting station. If we couln't get
        // to the current station, then no station in between the start and this
        // station would provide enough gas, so we can try starting at the next
        // station and begin again with an empty tank;
        if (tank < 0) {
            start = curr + 1;
            tank = 0;
        }
    }

    // If the ALL of the gas is not as much as the total cost, then a round trip
    // is not possible.
    if (total >= 0) return start;
    return -1;
};

module.exports = { canCompleteCircuit, canCompleteCircuit1 };
