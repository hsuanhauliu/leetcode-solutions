#include <iostream>
#include "Solution.h"

using namespace std;

void print_vals(vector< vector<int> > vals) {
	if (vals.size() == 0) {
		cout << "No values\n";
		return;
	}

	for(int i = 0; i < vals.size(); i++) {
		for (int j = 0; j < vals[i].size(); j++) {
			cout << vals[i][j] << " ";
		}
		cout << endl;
	}
	return;
}

int main() {
	Solution s = Solution();
	TreeNode* root = new TreeNode(3);
	root->left = new TreeNode(9);
	root->right = new TreeNode(20);
	root->right->left = new TreeNode(15);
	root->right->right = new TreeNode(7);

	cout << "First result:\n";
	vector< vector<int> > orders = s.levelOrderBottom(root);
	print_vals(orders);

	cout << "Second result:\n";
	TreeNode* new_root = NULL;
	vector< vector<int> > new_orders = s.levelOrderBottom(new_root);
	print_vals(new_orders);

	return 0;
}
