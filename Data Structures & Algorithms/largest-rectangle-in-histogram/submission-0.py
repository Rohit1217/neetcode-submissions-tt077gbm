class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_result=[1]*len(heights)
        left_stack=[]
        left_stack.append((0,heights[0]))

        for i in range(1,len(heights)):
            curr_elem=heights[i]
            idx,val=left_stack[-1]

            while curr_elem<val and len(left_stack)>0:
                left_result[idx]=i-idx
                left_stack.pop()
                if len(left_stack)==0:
                    idx,val=-1,-1
                else:
                    idx,val=left_stack[-1]

            left_stack.append((i,curr_elem))
        while len(left_stack)>0:
            idx,val=left_stack.pop()
            left_result[idx]=len(heights)-idx

        heights.reverse()
        right_result=[1]*len(heights)
        right_stack=[]
        right_stack.append((0,heights[0]))

        for i in range(1,len(heights)):
            curr_elem=heights[i]
            idx,val=right_stack[-1]

            while curr_elem<val and len(right_stack)>0:
                right_result[idx]=i-idx
                right_stack.pop()
                if len(right_stack)==0:
                    idx,val=-1,-1
                else:
                    idx,val=right_stack[-1]

            right_stack.append((i,curr_elem))
        while len(right_stack)>0:
            idx,val=right_stack.pop()
            right_result[idx]=len(heights)-idx
        
        right_result.reverse()
        heights.reverse()
        bias=[-1]*len(heights)
        combined=zip(left_result,right_result,heights)
        result=[(left+right-1)*height for left,right,height in combined]
        print(result)
        return max(result)