package main

func equalPairs(grid [][]int) int {
	// Determine the size of the grid (assuming it's a square grid)
	n := len(grid)

	// Temporary array to store row or column data
	temp := [200]int{}

	// Map to store the frequency of each row pattern
	rows := make(map[[200]int]int)

	// Iterate over each row in the grid
	for _, row := range grid {
		// Copy the current row into the temporary array
		copy(temp[:], row)

		// Increment the count of this row pattern in the map
		rows[temp]++
	}

	// Initialize a counter for the number of equal row-column pairs
	c := 0

	// Iterate over each column index
	for cidx := 0; cidx < n; cidx++ {
		// Temporary array to hold column data
		temp = [200]int{}

		// Construct the column by iterating over each row
		// Get the element at the same column index from each row
		for ridx := 0; ridx < n; ridx++ {
			// Assign the element from the current row to the temp array column
			temp[ridx] = grid[ridx][cidx]
		}
		// After the loop above, the temp column is made

		// Check if this temp column pattern exists in the row map
		if _, ok := rows[temp]; ok {
			// If it exists, add the count of this pattern to the counter
			c += rows[temp]
		}
	}

	// Return the total count of equal row-column pairs
	return c
}
