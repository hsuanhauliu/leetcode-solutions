# Minimum Path Sum
| #   | Description                                             | Difficulty | Solution File |
| --- | ------------------------------------------------------- | ---------- | ------------- |
| 64  | [Link](https://leetcode.com/problems/minimum-path-sum/) | Medium     | solution.py   |

## Additional Notes
Time Complexity: O(N),
Space Complexity: O(N),
where N is the number of cells the grid has.

### Observations
Since we can only move right and down, all cells can only be reached from up and left (except for the top row and the left-most column).

### Solution
This is a typical DP problem. We can calculate the minimum path sum by continuously choosing the smaller number between the left cell and the cell above, and that would give us the minimum path sum to the current cell. Once we finish iterating through all cells, the last cell would have the minimum path sum of the end cell.