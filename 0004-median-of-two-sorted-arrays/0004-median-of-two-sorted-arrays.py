class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_num = nums1 + nums2
        new_num.sort()
        if len(new_num) % 2 != 0:
            return new_num[int(len(new_num) // 2)]
        else:
            return  (new_num[int(len(new_num) // 2)] + new_num[int(len(new_num) // 2 - 1)])/2
        return 