class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        table = set(wordDict)
        dp = [False] * (length + 1)
        dp[0] = True
        
        for split_point in range(length):
            for tail in range(split_point + 1, length + 1):
                if dp[split_point] and s[split_point:tail] in table:
                    dp[tail] = True
        return dp[-1]