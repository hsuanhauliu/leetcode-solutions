class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_copy = set(banned)
        characters = "!?',;."
        for c in characters:
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower()

        words = paragraph.split()
        word_counter = {}

        for w in words:
            if w not in banned_copy:
                word_counter[w] = word_counter.get(w, 0) + 1
        return max(word_counter, key=word_counter.get)
