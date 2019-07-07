class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """ Recursively find all valid partitions """
        res = []
        self.find_all_palin(s, [], res)
        return res
    
    
    def find_all_palin(self, curr_str, curr_path, all_palin):
        if not curr_str:
            all_palin.append(curr_path)
            return
        
        for i in range(1, len(curr_str) + 1):
            if self.is_palin(curr_str[:i]):
                self.find_all_palin(curr_str[i:], curr_path + [curr_str[:i]], all_palin)
        return
    
    
    def is_palin(self, my_str):
        return my_str == my_str[::-1]