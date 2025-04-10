package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type NodeDepth struct {
	node  *TreeNode
	depth int
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	queue := []NodeDepth{}
	queue = append(queue, NodeDepth{root, 1})
	maxDepth := 1

	for len(queue) > 0 {
		node := queue[0].node
		depth := queue[0].depth
		maxDepth = max(maxDepth, depth)

		if node.Left != nil {
			queue = append(queue, NodeDepth{node.Left, depth + 1})
		}
		if node.Right != nil {
			queue = append(queue, NodeDepth{node.Right, depth + 1})
		}
		queue = queue[1:]
	}
	return maxDepth
}
