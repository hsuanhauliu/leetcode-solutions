class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        def get_divisors():
            d = [1]
            i = 2
            while i * i < num:
                if num % i == 0:
                    d.append(i)
                    d.append(num // i)
                i += 1
                
            if i * i == num:
                d.append(i)
                
            return d
        
        return sum(get_divisors()) == num