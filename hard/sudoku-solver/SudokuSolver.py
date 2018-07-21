class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        blank_cells = [] # a list of blank cells

        for r in xrange(9):
            for c in xrange(9):
                if board[r][c] == ".":
                    blank_cells.append((r, c))
        self.solve_next(blank_cells, board)

        return

    def solve_next(self, blank_cells, board):
        """
            Recurrence method for solving each cell.
        """
        # return true when we reach the leave node
        if blank_cells == []:
            return True

        cell = blank_cells.pop() # get next cell
        moves = self.calculate_moves(cell, board) # get a list of possible moves for this cell

        # try every move
        while moves:
            board[cell[0]][cell[1]] = moves.pop()
            if self.check_board(cell, board):
                if self.solve_next(blank_cells, board):
                    return True

        # none of the cell works, so we reset this cell go back to the parent node
        board[cell[0]][cell[1]] = "."
        blank_cells.append(cell)
        return False

    def check_board(self, (row, col), board):
        """
            Check if the move is valid by finding duplicates in row, column, and section.
        """
        checklist = []

        # check row
        for c in xrange(9):
            number = board[row][c]
            if number != ".":
                if number in checklist:
                    #print "duplicate in row"
                    return False
                else:
                    checklist.append(number)

        del checklist[:] # clear list

        # check column
        for r in xrange(9):
            number = board[r][col]
            if number != ".":
                if number in checklist:
                    #print "duplicate in column"
                    return False
                else:
                    checklist.append(number)
            
        del checklist[:] # clear list

        # check section
        temp_r = row / 3 * 3
        section_c = col / 3 * 3
        for r in xrange(3):
            section_r = temp_r + r
            for c in xrange(3):
                number = board[section_r][section_c + c]
                if number != ".":
                    if number in checklist:
                        #print "duplicate in section"
                        return False
                    else:
                        checklist.append(number)
                
        return True

    def calculate_moves(self, position, board):
        """
            Return a list of valid/possible moves for a cell.
        """
        invalid_moves = [] # list of numbers that are already in the neighboring row, column, section
        valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # return variable

        # check row
        for c in xrange(9):
            current = board[position[0]][c]
            if current != ".":
                invalid_moves.append(current)

        # check col
        for r in xrange(9):
            current = board[r][position[1]]
            if current != "." and current not in invalid_moves:
                invalid_moves.append(current)

        # check block
        start_row = position[0] - position[0] % 3
        start_col = position[1] - position[1] % 3
        for r in xrange(3):
            curr_row = start_row + r
            for c in xrange(3):
                curr_col = start_col + c
                current = board[curr_row][curr_col]
                if current != "." and current not in invalid_moves:
                    invalid_moves.append(current)

        # remove invalid_moves
        for n in invalid_moves:
            valid_moves.remove(n)

        return valid_moves
