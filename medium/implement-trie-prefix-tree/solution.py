class Trie:
    class Node:
        def __init__(self, val):
            self.val = val
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = self.Node(0)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_children = self.tree.children
        for char in word:
            if char not in curr_children:
                curr_children[char] = self.Node(char)
            curr_children = curr_children[char].children
                
        curr_children[0] = 0    # add stop word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        found, curr_children = self.__foundLastNodes(word)
        return found and 0 in curr_children
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.__foundLastNodes(prefix)[0]
    
    
    def __foundLastNodes(self, prefix):
        curr_children = self.tree.children
        for char in prefix:
            if char not in curr_children:
                return False, {}
            curr_children = curr_children[char].children
            
        return True, curr_children
    
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)