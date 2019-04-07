class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        all_permutations = []
        self.permute_recursive(s, 0, "", all_permutations)
        return all_permutations


    def permute_recursive(self, s, pos, curr, all_p):
        """ Recursively build the string while checking for letters one character at a time. """
        while pos != len(s):
            if s[pos].isalpha():
                self.permute_recursive(s, pos + 1, curr + s[pos].lower(), all_p)
                self.permute_recursive(s, pos + 1, curr + s[pos].upper(), all_p)
                return
            curr += s[pos]
            pos += 1
        all_p.append(curr)


def main():
    sol = Solution()
    print(sol.letterCasePermutation("a1b2"))
    print(sol.letterCasePermutation("A1b2"))
    print(sol.letterCasePermutation(""))
    print(sol.letterCasePermutation("1234"))
    print(sol.letterCasePermutation("z"))


if __name__ == "__main__":
    main()
