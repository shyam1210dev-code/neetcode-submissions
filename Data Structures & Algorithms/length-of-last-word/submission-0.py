class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_string=s.strip()

        word_list=s.split()
        return len(word_list[-1])  