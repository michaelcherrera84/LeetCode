import Cocoa

/// Definition for a binary tree node.
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() {
        self.val = 0
        self.left = nil
        self.right = nil
    }
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {

    /// Given the `root` of a Binary Search Tree (BST), return *the minimum
    /// absolute difference between the values of any two different nodes in
    /// the tree*.
    /// - Parameter root: the root of a Binary Search Tree
    /// - Returns: the minimum absolute difference between the values of any
    /// two different nodes in the tree
    func getMinimumDifference(_ root: TreeNode?) -> Int {
        var prev: Int? = nil
        var diff: Int = Int.max


        /// Since a BST is an ordered tree, the minimum difference between
        /// nedes will always be between a node and the node immediately
        /// preceeding it in order.
        /// - Parameter node: the current node
        func traverse(_ node: TreeNode?) {
            guard let node else { return }

            // The lowest value node is to the far left.
            traverse(node.left)

            // If prev is nil, we are on the lowest value node and there is
            // no previous node to calculate the difference.
            if let prev = prev {
                // If the difference between this node and the previous node
                // is less than the current minimum difference, set the current
                // minimum difference to this difference.
                diff = min(diff, node.val - prev)
            }

            // Set the previous node to this node before moving on.
            prev = node.val
            traverse(node.right)
        }

        // Traverse the tree recursively to find the minimum difference.
        traverse(root)
        return diff
    }
}

let sol = Solution()

/// Example 1 - [4,2,6,1,3]
var root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
sol.getMinimumDifference(root)

/// Example 2 - [1,0,48,null,null,12,49]
root = TreeNode(4, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
sol.getMinimumDifference(root)

/// Minimum difference in [100000, 0] is 100000
root = TreeNode(100_000, TreeNode(0), nil)
sol.getMinimumDifference(root)
