class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        cur = []

        def Try(t, target):
            if len(cur) > k:
                return
            if target == 0 and len(cur) == k:
                res.append(cur[::]) 

            try:
                for i in range(t + 1,10): 
                    
                    cur.append(i)

                    Try(i,target - i)
                    cur.pop()
 
            except:
                return

        Try(0,n)
        return res

        