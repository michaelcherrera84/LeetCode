package _00637_AverageOfLevelsInBinaryTree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 */
@SuppressWarnings("unused")
class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

@SuppressWarnings("unused")
public class Solution {

    /**
     * Given the {@code root} of a binary tree, return <i>the average value of
     * the nodes on each level in the form of an array</i>.
     *
     * @param root the root of a binary tree
     * @return the average value of the nodes on each level
     */
    List<Double> averageOfLevels(TreeNode root) {
        List<Double> averages = new ArrayList<>();      // list of average values
        Queue<TreeNode> nodes = new LinkedList<>();     // nodes waiting to add
        
        nodes.offer(root);

        // Loop while there are still nodes to value.
        while (!nodes.isEmpty()) {
            int count = nodes.size();  // number of nodes at this level
            double sum = 0.0;          // sum of nodes at this level

            // For each node at this level, add the value to the sum.
            for (int i = 0; i < count; i++) {
                TreeNode curr = nodes.poll();
                
                sum += curr.val;
                
                // If there is a level below this level, add the nodes to the queue.
                if (curr.left != null) {
                    nodes.offer(curr.left);
                }
                if (curr.right != null) {
                    nodes.offer(curr.right);
                }
            }

            // When the loop is complete, all of the nodes at the current level 
            // have been counted and summed. Add the average to the list.
            averages.add(sum / count);
        }

        return averages;
    }
}
