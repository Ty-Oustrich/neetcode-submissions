class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencyBuckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 +count.get(num,0)
        for n, c in count.items():
            frequencyBuckets[c].append(n)    

        res = []
        for i in range(len(frequencyBuckets) -1,0,-1):
            for num in frequencyBuckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
