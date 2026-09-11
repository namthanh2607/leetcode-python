class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans =[]
        for i in range(len(digits)):
            if i > 1 and digits[i]==digits[i-1]:
                continue
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i!=k and j!=k:
                        if digits[i]!=0 and digits[k] %2==0 and 100*digits[i]+10*digits[j]+digits[k] not in ans:
                            ans.append(100*digits[i]+10*digits[j]+digits[k])
        return len(ans)