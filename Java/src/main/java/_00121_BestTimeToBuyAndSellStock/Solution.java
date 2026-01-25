package _00121_BestTimeToBuyAndSellStock;

public class Solution {

    /**
     * Given an array {@code prices} where {@code prices[i]} is the price of a
     * given stock on the {@code ith} day, maximize your profit by choosing a
     * <b>single day</b> to buy one stock and choosing a
     * <b>different day in the future</b> to sell that stock.
     *
     * @param prices the array of prices
     * @return the maximum profit you can achieve from this transaction, or 0 if
     * no profit is possible.
     */
    public int maxProfit(int[] prices) {

        if (prices == null || prices.length == 0) {
            throw new IllegalArgumentException("The list of prices cannot be empty.");
        }

        int buy = prices[0];    // the price at which to buy
        int max = 0;            // the maximum profit

        // For each price...
        for (int i = 0; i < prices.length; i++) {

            // if it is lower than the current buy price, buy at this price instead.
            if (prices[i] < buy) {
                buy = prices[i];
            } 
            // If selling at the current price would result in a larger profit,
            // this profit is the next maximum profit.
            else if (prices[i] - buy > max) {
                max = prices[i] - buy;
            }

            // Note: This works because finding a new buy price does not affect the
            // the profit we've found so far. So a new lower buy price can only 
            // possibly result in either a larger profit later on, or we simply
            // keep the profit we already have.
        }

        return max;
    }
}
