class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rows = {}

        # Create array for reverse grid
        reverseGrid = [[] for _ in range(n)]
        for i in grid:
            # Store the rows as you read from grid
            rows[tuple(i)] = rows.get(tuple(i), 0) + 1
            for ridx, nestedGrid in enumerate(i):
                reverseGrid[ridx].append(nestedGrid)
        
        c = 0
        for i in reverseGrid:
            k = tuple(i)
            # if column array matches an original grid row, append the count of that row to c.
            # we do this because we are looking for how many times the column matches a row
            # so one column can match multiple rows, but a row can only match one column
            if k in rows:
                c += rows[k]

        return c