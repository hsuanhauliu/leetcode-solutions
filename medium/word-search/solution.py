class Solution:
    def exist(self, board, word):
        if len(word) == 0:
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find_word(board, i, j, word, 0):
                    return True
        return False

    def find_word(self, board, x, y, word, w_i):
        if w_i == len(word):
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[w_i]:
            return False

        board[x][y] = ""
        found = (self.find_word(board, x + 1, y, word, w_i + 1) or
                 self.find_word(board, x - 1, y, word, w_i + 1) or
                 self.find_word(board, x, y + 1, word, w_i + 1) or
                 self.find_word(board, x, y - 1, word, w_i + 1))
        board[x][y] = word[w_i]
        return found


def main():
    sol = Solution()
    print(sol.exist([['A','B','C','E'],
                     ['S','F','C','S'],
                     ['A','D','E','E']], 'ESE') == True)
    print(sol.exist([['A','B','C','E'],
                     ['S','F','C','S'],
                     ['A','D','E','E']], 'BCB') == False)


    # edge cases
    print(sol.exist([], '') == True)
    print(sol.exist([[]], '') == True)
    print(sol.exist([], 'A') == False)
    print(sol.exist([[]], 'A') == False)


if __name__ == '__main__':
    main()
