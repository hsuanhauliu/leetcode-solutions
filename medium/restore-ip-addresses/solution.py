class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def helper(s, remain, curr):
            if not remain:
                if not s:
                    res.append(".".join(curr))
                return

            for i in range(1, min(len(s) + 1, 4)):
                if i > 1 and s[0] == "0":
                    return

                if int(s[:i]) < 256:
                    helper(s[i:], remain-1, curr + [s[:i]])

        helper(s, 4, [])
        return res
