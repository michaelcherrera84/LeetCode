package _00373_FindKPairsWithSmallestSums;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Solution {

    /**
     * You are given two integer arrays {@code nums1} and {@code nums2} sorted in
     * <b>non-decreasing order</b> and an integer {@code k}.
     * <p>
     * Define a pair {@code (u, v)} which consists of one element from the first
     * array and one element from the second array.
     * <p>
     * Return <i>the</i> {@code k} <i>pairs</i>
     * {@code (u1, v1), (u2, v2), ..., (uk, vk)} <i>with the smallest sums</i>.
     * 
     * @param nums1 first integer array
     * @param nums2 second integer array
     * @param k     number of pairs
     * @return the number of pairs with the smallest sums
     */
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        // queue of arrays containing pair sums and the pair indices
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        List<List<Integer>> pairs = new ArrayList<>();

        // Add the smallest pair sum and the indices for each value of `nums1` 
        // up to `k` pairs to the queue.
        for (int i = 0; i < nums1.length && i < k; i++)
            pq.offer(new int[] { nums1[i] + nums2[0], i, 0 });

        // Add the smallest pair from the queue to the result pairs list. Then
        // add the next smallest pair sum and the indices to the queue.
        while (!pq.isEmpty() && pairs.size() < k) {
            int[] pair = pq.poll();
            int i = pair[1], j = pair[2];

            pairs.add(List.of(nums1[i], nums2[j]));

            if (j + 1 < nums2.length) {
                pq.offer(new int[] { nums1[i] + nums2[j + 1], i, j + 1 });
            }
        }

        return pairs;
    }
}