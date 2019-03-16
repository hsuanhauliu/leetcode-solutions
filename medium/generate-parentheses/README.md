# Generate Parentheses
| #   | Description                                                 | Difficulty | Solution File |
| --- | ----------------------------------------------------------- | ---------- | ------------- |
| 22  | [Link](https://leetcode.com/problems/generate-parentheses/) | Medium     | solution.py   |

## Additional Notes
### Observations
1. Obviously, we cannot add a right parenthesis without having a corresponding left parenthesis.
2. While constructing each string combination, the number of right parentheses are always left than or equal to that of left paretheses.
3. All strings are of length 2 * n.

### Solution
Using a recursion approach, there are three things to keep in mind: conditions, constraints, and base case. We want to construct each possible valid combination of parentheses. At each call, we can branch out two-way: adding a left or right parenthesis. We can only add up to n left parentheses, and add right parentheses when there are more left parentheses than left parentheses. The base case is of course adding the complete string to our list.