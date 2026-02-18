/**
 * Given and integer array `prices` where `prices[i]` is the price of a given
 * stock on the `ith`day, find *the **maximum** profit you can achieve*.
 *
 * On each day, you may decide to buy and/or sell the stock. You can only hold
 * *at most one* share of the stock at any time. However, you can sell and buy
 * the stock multiple times on the **same day**, ensuring you never hold more
 * than one share of the stock.
 * @param {number[]} prices integer array of stock prices
 * @returns {number} maximum achievable profit
 */
var maxProfit = function (prices) {
    let profit = 0;
    let buy = prices[0];

    // For each price, if the current price is higher than the buy price, add 
    // the difference to the profit. Always "buy" at each price to look for the 
    // next profit.
    prices.forEach((element) => {
        if (element > buy) {
            profit += element - buy;
        }

        buy = element;
    });

    return profit;
};

module.exports = { maxProfit };
