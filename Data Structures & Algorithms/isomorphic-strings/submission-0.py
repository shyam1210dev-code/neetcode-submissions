class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_t_dict = {}
        t_s_dict = {}

        for char_s,char_t in zip(s,t):
            if char_s in s_t_dict and s_t_dict[char_s] != char_t or char_t in t_s_dict and t_s_dict[char_t] != char_s:
                return False
            
            s_t_dict[char_s]=char_t
            t_s_dict[char_t]=char_s
        return True

        