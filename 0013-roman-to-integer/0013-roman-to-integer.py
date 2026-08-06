class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {
        "I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000
        }
        nums = 0
        for i in range(len(s)-1):
            if convert[s[i]] >= convert[s[i+1]]:
                nums += convert[s[i]]
            else:
                nums -= convert[s[i]]
        nums += convert[s[len(s)-1]]
        return nums
