class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """ Group bit lists if they are similar. Similarity is calculated
        by XORing the two lists. If it's all 1's or all 0's, they are
        considered similar. Return the size of the biggest group.
        
        Time: O(n^2) where n is the number of bit lists.
        Space: O(n)
        """
        size = len(matrix)
        mask = 2 ** len(matrix[0]) - 1
        nums = [self.convert_to_binary(l) for l in matrix]
        checked = set()
        buckets = []
        
        # Compare each pair
        for i in range(size):
            if i not in checked:
                checked.add(i)
                buckets.append(1)
                for j in range(i+1, size):
                    if self.is_similar(nums[i], nums[j], mask):
                        buckets[-1] += 1
                        checked.add(j)
        return max(buckets)
        
    
    def convert_to_binary(self, bit_list):
        return int(''.join(str(bit) for bit in bit_list), 2)
    
    
    def is_similar(self, num_1, num_2, mask):
        res = (num_1 ^ num_2) & mask
        return res == mask or not res