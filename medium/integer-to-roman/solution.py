class Solution:
    rls = {1: "I", 4: "IV", 5: "V", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC",
            100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        
    def intToRoman(self, num: 'int') -> 'str':
        roman = ""
        power = 1

        while num != 0:
            curr = num % 10
            num //= 10

            if curr > 4:
                if curr == 9:
                    roman = self.rls[9 * power] + roman
                else:
                    curr -= 5
                    roman = self.rls[5 * power] + curr * self.rls[power] + roman
            elif curr == 4:
                roman = self.rls[4 * power] + roman
            else:
                roman = curr * self.rls[power] + roman
            power *= 10
        return roman
