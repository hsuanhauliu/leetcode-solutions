/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <vector>
#include <queue>

using namespace std;

class Solution {
	public:
		vector< vector<int> > levelOrderBottom(TreeNode* root) {
			vector< vector<int> > orders;
			if (!root)
				return orders;
            
			queue<TreeNode*> myqueue;
			myqueue.push(root);

			while (!myqueue.empty()) {
				int num_of_iterations = myqueue.size();
				vector<int> level;

				for (int i = 0; i < num_of_iterations; i++) {
					TreeNode* curr_node = myqueue.front();

					if (curr_node->left != NULL) {
						myqueue.push(curr_node->left);
					}
					if (curr_node->right != NULL) {
						myqueue.push(curr_node->right);
					}

					level.push_back(curr_node->val);	// add value
					myqueue.pop();	// toss it away once we're done
				}
				orders.insert(orders.begin(), level);
			}

			return orders;
		}
};
