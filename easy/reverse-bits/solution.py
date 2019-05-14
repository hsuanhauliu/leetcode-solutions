class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b_str = bin(n)[2:]
        b_str = '0' * (32 - len(b_str)) + b_str
        bits = [c for c in b_str]
        length = len(bits)
        
        for i in range(length // 2):
            if bits[i] != bits[length - 1 - i]:
                temp = bits[i]
                bits[i] = bits[length - 1 - i]
                bits[length - 1 - i] = temp
        
        return int("".join(bits), 2)

