class Solution {
	public boolean isValidSudoku(char[][] board) {
		// check rows
		for (int r = 0; r < 9; r++) {
			int[] temp = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
			for (int c = 0; c < 9; c++) {
				char num = board[r][c];

				// if we have already seen this number
				if (num != '.') {
					int intnum = num - '0';
					if (temp[intnum] == 1)
						return false;
					else
						temp[intnum] = 1;
				}
			}
		}

		// check columns
		for (int c = 0; c < 9; c++) {
			int[] temp = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
			for (int r = 0; r < 9; r++) {
				char num = board[r][c];

				// if we have already seen this number
				if (num != '.') {
					int intnum = num - '0';
					if (temp[intnum] == 1)
						return false;
					else
						temp[intnum] = 1;
				}
			}
		}

		// check sub-box
		for (int br = 0; br < 3; br++) {
			for (int bc = 0; bc < 3; bc++) {
				int [] temp = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
				for (int counter1 = 0; counter1 < 3; counter1++) {
					for (int counter2 = 0; counter2 < 3; counter2++) {
						char num = board[br * 3 + counter1][bc * 3 + counter2];

						if (num != '.') {
							int intnum = num - '0';
							if (temp[intnum] == 1)
								return false;
							else
								temp[intnum] = 1;
						}
					}
				}
			}
		}

		return true;            
	}
}
