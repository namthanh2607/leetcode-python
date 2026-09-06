class Solution:
    def jump(self, nums: List[int]) -> int:
        max_posi = []

        leng = len(nums)
        if leng == 1:
            return 0
        for i in range(leng):
            max_posi.append(i + nums[i])

        val = max_posi[0]
        step = 1
        print(max_posi)
        while val < leng - 1:
            val = max(max_posi[:val + 1])
            step += 1

        return step


                        