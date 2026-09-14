class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1 = rec1[0],rec1[1]
        x2,y2 = rec1[2],rec1[3]
        x3,y3 = rec2[0],rec2[1]
        x4,y4 = rec2[2],rec2[3]
        check_x = not(x2 <= x3 or x1 >= x4)
        check_y = not(y2 <= y3 or y1 >= y4)
        print(check_x,check_y)
        return check_x and check_y
       

        