class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_count={}

        for num in nums:
            if num in nums_count:
                nums_count[num]+=1
            else:
                nums_count[num]=1
        
        sorted_keys = sorted(nums_count, key=lambda num: nums_count[num], reverse=True)
        return sorted_keys[:k]