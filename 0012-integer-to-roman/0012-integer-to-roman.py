class Solution:
    def intToRoman(self, num):
        ans = ""
        ptu_1 = num // 1000
        ptu_2 = (num - ptu_1 * 1000) // 100 
        ptu_3 = (num - ptu_1 * 1000 - ptu_2 * 100) // 10 
        ptu_4 = (num - ptu_1 * 1000 - ptu_2 * 100 - ptu_3 * 10) 
        #hang nghin
        ans += ptu_1 * "M"
        #hang tram
        if ptu_2 in [5,6,7,8]:
            ans += "D" + (ptu_2 - 5)* "C" 
        elif ptu_2 == 9 :
            ans += "CM"
        elif ptu_2 == 4 :
            ans += "CD"
        else:
            ans += ptu_2* "C"
        #hang chuc
        if ptu_3 in [5,6,7,8]:
            ans += "L" + (ptu_3 - 5)* "X" 
        elif ptu_3 == 9 :
            ans += "XC"
        elif ptu_3 == 4 :
            ans += "XL"
        else:
            ans += ptu_3 * "X"
        #hang don vi
        if ptu_4 in [5,6,7,8]:
            ans += "V" + (ptu_4 - 5)* "I" 
        elif ptu_4 == 9 :
            ans += "IX"
        elif ptu_4 == 4 :
            ans += "IV"
        else:
            ans += ptu_4 * "I"
        return ans