class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        if not digits:
            return []

        letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                   "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        all_combinations = []
        self.find_combination_recursive(digits, letters, all_combinations, "")
        return all_combinations

    def find_combination_recursive(self, d, letters, a, curr):
        if not d:
            a.append(curr)
            return
        
        for l in letters[d[0]]:
            self.find_combination_recursive(d[1:], letters, a, curr + l)
