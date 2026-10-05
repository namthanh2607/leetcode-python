class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char for char in s if char.isalnum())
        res = res.lower()
        return res[::-1] == res


        