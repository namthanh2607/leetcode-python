class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst = list(map(str, nums))
        lst.sort(key = lambda x: x*10, reverse = True)
        if lst[0] == "0":
            return "0"
        ret = ''.join(lst)
        return ret

                

        