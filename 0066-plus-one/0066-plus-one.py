class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        check = True
        while check:
            if digits[i] != 9:
                digits[i] += 1
                check = False
            elif digits[i] == 9:
                if i + len(digits) != 0:
                    digits[i] = 0
                    i = i - 1
                else:
                    digits[i] = 0
                    digits = [1] + digits
                    check = False
        return digits

        