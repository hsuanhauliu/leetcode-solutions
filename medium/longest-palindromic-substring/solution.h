#include <string>

using namespace std;

class Solution {
public:
	string longestPalindrome(string s) {
		string longest;
		string str;

		for (int i = 0; i < s.size(); i++) {
			str = findPalindrome(s, i, i);
			if (str.size() > longest.size()) {
				longest = str;
			} 

			str = findPalindrome(s, i, i + 1);
			if (str.size() > longest.size()) {
				longest = str;
			} 
		}
		return longest; 
	}

private:
	string findPalindrome(string s, int left, int right)
	{
		while (left > -1 && right < s.size() && s[left] == s[right]) {
			left--;
			right++;
		}
		return s.substr(left + 1, right - left - 1);
	}
};

