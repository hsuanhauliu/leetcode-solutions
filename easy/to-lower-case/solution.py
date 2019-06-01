class Solution:
    def toLowerCase(self, str: str) -> str:
        """ Convert characters within bound in one line"""
        return "".join([chr(ord(char) + 32) if ord('A') <= ord(char) and ord(char) <= ord('Z') else char for char in str])