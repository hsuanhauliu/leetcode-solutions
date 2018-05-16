#include <vector>

using namespace std;

class Solution {
	public:
		void rotate(vector<vector<int> >& matrix) {
			int end = matrix.size() - 1;
			for (int r = 0; r < matrix.size() / 2; r++) {
				for (int c = r; c < end - r; c++) {
					int temp = matrix[r][c];
					matrix[r][c] = matrix[end - c][r];
					matrix[end - c][r] = matrix[end - r][end - c];
					matrix[end - r][end - c] = matrix[c][end - r];
					matrix[c][end - r] = temp;
				}
			}
		}
};
