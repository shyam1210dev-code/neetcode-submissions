class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy=nums.copy()

        for num in nums_copy:
            nums.append(num)

        return nums
        