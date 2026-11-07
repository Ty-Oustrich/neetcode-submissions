class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            result_list = []
            completing_partner = target - nums[i]
            if completing_partner in nums and nums.index(completing_partner) != i:
                result_list.append(i)
                result_list.append(nums.index(completing_partner))
                result_list.sort() 
                return result_list

