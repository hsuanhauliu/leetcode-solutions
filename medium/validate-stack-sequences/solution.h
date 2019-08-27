#include <stack>

using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        /*
            Straightforward solution: push and pop.
            
            Time: O(n)
            Space: O(n)
        */
        stack<int> my_stack;
        int i = 0;
        int j = 0;
        int size = pushed.size();
        
        while (i < size) {
            if (my_stack.empty() || my_stack.top() != popped[j]) {
                my_stack.push(pushed[i]);
                i++;
            }
            else {
                my_stack.pop();
                j++;
            }
        }
        
        while (j < size) {
            if (my_stack.top() == popped[j]) {
                my_stack.pop();
                j++;
            }
            else {
                return false;
            }
        }
        return true;
    }
};