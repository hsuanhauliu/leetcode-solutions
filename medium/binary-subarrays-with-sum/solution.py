class Solution(object):
    """
    This is an example of prefix-sum problem. We are counting the number of subarrays
    that have sum of S. We know that A[0, j] = A[0] + A[1] + ... + A[j], and therefore
    A[i, j] = A[0, j] - A[0, i]. The number of i, j pairs that satisfy A[i, j] = S is
    what we are looking for. We can use an array of size N + 1 to keep track the num
    of subarrays that sum to its array index. For example, pre_sum[3] = 5 means that
    there are 5 A[0, i] subarrays that sum to its index, 3. By re-arranging the
    equation from earlier, we get A[0, i] = A[0, j] - A[i, j]. For each iteration, we
    calculate the current sum minus our target S, A[0, j] - S, which equals to A[0, i],
    the remaining sum. Then, we can look up pre_sum table to find out how many
    subarrays have the sum of A[0, i].
    """

    def numSubarraysWithSum(self, a, s):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        total = 0       # number of valid subarrays sums to s
        curr_sum = 0    # sum of a[0, i]
        pre_sum = [0] * (len(a) + 1)    # remember number of arrays sums to its index
        pre_sum[0] = 1  # let the number of subarray that sums to 0 be 1
        
        for i in range(len(a)):
            curr_sum += a[i]
            if curr_sum >= s:
                total += pre_sum[curr_sum - s]
            pre_sum[curr_sum] += 1
            
        return total