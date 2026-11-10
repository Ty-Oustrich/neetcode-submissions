class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums == nums.sort()
        numset = set(nums)
        for num in nums:
            if not num-1 in numset:
                hold = 1
                while num+1 in numset:
                    hold += 1
                    num +=1
                if hold > answer:
                    answer = hold

        return answer
                
