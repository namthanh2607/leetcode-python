class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        cur = []
        def Try(k,leng):

            if leng == 0 :
                res.append(cur[::])
                return

            for i in range(1,leng + 1):
                if s[k : k + i] == s[k : k + i][::-1]:
                    cur.append(s[k:k + i])
                    Try(k + i,leng - i)
                    cur.pop()


        Try(0,len(s))
        return res

        
        