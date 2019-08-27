/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        if (!root) {
            return res;
        }
        
        vector<Node*> curr_q;
        curr_q.push_back(root);
        while (!curr_q.empty()) {
            vector<Node*> next_q;
            vector<int> vals;
            for (Node* node : curr_q) {
                vals.push_back(node->val);
                for (Node* child : node->children) {
                    next_q.push_back(child);
                }
            }
            res.push_back(vals);
            curr_q = next_q;
        }
        return res;
    }
};