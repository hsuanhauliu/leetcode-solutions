#include <iostream>

using namespace std;

class Solution {
	public:
		bool isUgly(int num) {
			if (num < 1)
				return false;

			int primes[] = {2, 3, 5};
			
			for (int i = 0; i < 3; i++)
				while (num % primes[i] == 0)
					num /= primes[i];

			if (num == 1)
				return true;
			return false;
		}
};

int main() {
	Solution s = Solution();
	cout << s.isUgly(0) << endl;
	return 0;
}

