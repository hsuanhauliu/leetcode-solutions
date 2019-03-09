# Jump Game
| #   | Description                                      | Difficulty | Solution File |
| --- | ------------------------------------------------ | ---------- | ------------- |
| 55  | [Link](https://leetcode.com/problems/jump-game/) | Medium     | solution.py   |

## Additional Notes
### Observations
1. Every number needs to be examined to determine whether we can reach the end or not.
2. Since each element represents the furtherest jump from that cell, we should also be able to reach every cell before the furtherest cell that we can reach from current cell. Thus, if there is ever a cell we cannot reach, all the cells behind it will not be reachable.

### Solution
To determine whether the end cell is reachable, we can simply keep track of the furthest position that we can reach while iterating through all the elements. If there ever is a cell where we previously cannot reach, then the end cell is not reachable, and therefore we return false. If we can successfully finish iterating through all elements, it means that we can reach the end cell. Thus, we return true.