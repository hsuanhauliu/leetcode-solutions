class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(size // 2):
            s[i], s[size-1-i] = s[size-1-i], s[i]