class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            result_list = []
            cp = target - nums[i]
            if cp in nums and nums.index(cp) != i:
                result_list.append(i)
                if nums.index(cp) != i:
                    result_list.append(nums.index(cp))
                    result_list.sort() 
                    return result_list


        



            