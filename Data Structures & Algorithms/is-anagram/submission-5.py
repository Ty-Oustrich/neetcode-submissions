class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        counts_t = {}

        for char in s:
            counts_s[char] = counts_s.get(char, 0) + 1


        for char in t:
            counts_t[char] = counts_t.get(char, 0) + 1

        return counts_t == counts_s