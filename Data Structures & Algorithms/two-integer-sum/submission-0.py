class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums_dict={}

        for index,num in enumerate(nums):
            required_num=target-num
            if required_num in index_nums_dict:
                return [index_nums_dict[required_num],index]
            
            index_nums_dict[num]=index

        
        return []
        