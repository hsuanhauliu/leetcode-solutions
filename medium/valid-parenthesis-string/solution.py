class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p, stars = [], []
        for i, char in enumerate(s):
            if char == '(':
                left_p.append(i)
            elif char == '*':
                stars.append(i)
            else:
                if left_p:
                    left_p.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        p_i, star_i, num_star = 0, 0, len(stars)
        while p_i < len(left_p):
            # skip any star that's on the left side
            while star_i < num_star and stars[star_i] < left_p[p_i]:
                star_i += 1
            if star_i < num_star:
                p_i += 1
                star_i += 1
            else:
                return False
        return True