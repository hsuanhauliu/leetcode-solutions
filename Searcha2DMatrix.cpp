class Solution {
	public:
		bool searchMatrix(vector< vector<int> >& matrix, int target) {
			int start = 0;
			int end = matrix.size();
			int mid = (start + end) / 2;

			if (end == 0 || matrix[0].size() == 0) {
				return false;
			}

			while (start != mid) {
				int compare = matrix[mid][0];

				if (target < compare) {
					end = mid;
				}
				else if (compare < target) {
					start = mid;
				}
				else {
					return true;
				}
				mid = (start + end) / 2;
			} 

			start = 0;
			end = matrix[mid].size();
			int mid_mid = (start + end) / 2;

			while (start != mid_mid) {
				int compare = matrix[mid][mid_mid];

				if (target < compare) {
					end = mid_mid;
				}
				else if (compare < target) {
					start = mid_mid;
				}
				else {
					return true;
				}
				mid_mid = (start + end) / 2;
			}
			
			if (matrix[mid][mid_mid] == target)
				return true;

			return false;
		}
};
