package main

import (
	"slices"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}

	r1Leaves := getLeaves(root1)
	r2Leaves := getLeaves(root2)
	return slices.Equal(r1Leaves, r2Leaves)
}

func getLeaves(root *TreeNode) []int {
	queue := []*TreeNode{root}
	leaves := []int{}

	for len(queue) > 0 {
		node := queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		if node.Left == nil && node.Right == nil {
			leaves = append(leaves, node.Val)
		}
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
	return leaves
}
