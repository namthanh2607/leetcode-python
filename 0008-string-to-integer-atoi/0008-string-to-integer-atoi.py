class Solution:
    def myAtoi(self, s: str) -> int:
        nums = ""
        for i in s:
            if nums == "":
                if i not in ["+","-","0","1","2","3","4","5","6","7","8","9"," "]:
                    break
                elif i == " ":
                    continue
                else:
                    nums += i
            elif nums != "":
                if i not in ["0","1","2","3","4","5","6","7","8","9"]:
                    break
                else:
                    nums += i
        if nums == "":
            return 0
        elif nums in ["+","-"]:
            return 0
        elif int(nums)> 2**31 -1:
            return 2**31 -1
        elif int(nums) < -2**31:
            return -2**31
        else:
            return int(nums)          

