#include "solution.h"
#include <iostream>

using namespace std;

int main() {
	Solution sol;
	string test1 = "babad";
	string test2 = "cbbd";
	string test3 = "a";
	string test4 = "";

	cout << "Output 1: " << sol.longestPalindrome(test1) << endl;
	cout << "Output 2: " << sol.longestPalindrome(test2) << endl;
	cout << "Output 3: " << sol.longestPalindrome(test3) << endl;
	cout << "Output 4: " << sol.longestPalindrome(test4) << endl;
	return 0;
}
