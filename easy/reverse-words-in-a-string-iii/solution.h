using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        /* Two-pass approach. Find indices of all spaces one the first part
        including the end of line. Next, reverse each word one by one.
        
        Time: O(n)
        Space: O(n)
        */
        vector<int> breaks = find_break_indices(s);
        int prev = 0;
        for (int j = 0; j < breaks.size(); j++) {
            int curr = breaks[j] - 1;
            while (prev < curr) {
                char temp = s[prev];
                s[prev] = s[curr];
                s[curr] = temp;
                prev++;
                curr--;
            }
            prev = breaks[j] + 1;
        }
        return s;
    }
    
    vector<int> find_break_indices(string s) {
        vector<int> breaks;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                breaks.push_back(i);
            }
        }
        breaks.push_back(s.size());
        return breaks;
    }
};