class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleant = "".join(filter(str.isalnum, s)).lower()
        reverse = "".join(cleant[::-1])
        for i in range(len(cleant)//2):
            if (cleant[i] != reverse[i]):
                return False
        return True
