#include <string>
#include <map>

using namespace std;

class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		map<char, int> lookup;
		int max_length = 0;
		int last_pos = -1;

		for (int i = 0; i < s.size(); i++) {
			if (lookup.find(s[i]) != lookup.end() && last_pos < lookup[s[i]]) {
				last_pos = lookup[s[i]];
			}

			if (i - last_pos > max_length) {
				max_length = i - last_pos;
			}
			lookup[s[i]] = i;
		}
		return max_length;
	}
};
