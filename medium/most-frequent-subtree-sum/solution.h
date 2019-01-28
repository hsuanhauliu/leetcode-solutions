#include <vector>
#include <unordered_map>
#include <map>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
		if (root == NULL) {
			return vector<int>();
		}

		unordered_map<int, int> subtree_sums;
		map<int, vector<int> > counts;
		findSubtreeSum(root, subtree_sums);

		for (auto it = subtree_sums.begin(); it != subtree_sums.end(); ++it) {
			if (counts.find(it->second) == counts.end()) {
				counts.insert(pair<int, vector<int> > (it->second, vector<int>()));
			}
			counts[it->second].push_back(it->first);
		}

        return counts.rbegin()->second;
    }

	int findSubtreeSum(TreeNode* root, unordered_map<int, int> &subtree_sums) {
		if (root == NULL) {
			return 0;
		}

		int my_sum = root->val + findSubtreeSum(root->left, subtree_sums) + findSubtreeSum(root->right, subtree_sums);
		if (subtree_sums.find(my_sum) == subtree_sums.end()) {
			subtree_sums[my_sum] = 1;
		}
		else {
			subtree_sums[my_sum]++;
		}

		return my_sum;
	}
};
