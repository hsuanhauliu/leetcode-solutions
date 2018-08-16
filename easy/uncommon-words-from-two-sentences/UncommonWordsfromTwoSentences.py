class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        occurrences = {}
        sentence = A + " " + B
        words = sentence.split()

        for w in words:
            if w not in occurrences.keys():
                occurrences[w] = 1
            else:
                occurrences[w] += 1

        uncommon = []
        for word, occur in occurrences.items():
            if occur == 1:
                uncommon.append(word)

        return uncommon

