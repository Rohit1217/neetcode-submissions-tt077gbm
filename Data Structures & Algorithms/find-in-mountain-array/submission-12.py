class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        left=0
        right=mountainArr.length()-1
        peak=None

        mid=(left+right)//2
        print(left,right,right-left+1)

        while (right-left+1)>3:
            mid=(left+right)//2

            if mountainArr.get(mid-1)<mountainArr.get(mid) and mountainArr.get(mid)>mountainArr.get(mid+1):
                peak=mid
                break
            elif mountainArr.get(mid-1)<mountainArr.get(mid)<mountainArr.get(mid+1):
                left=mid+1
            else:
                right=mid-1
        
        if peak is None:
            if mountainArr.get(mid-1)>mountainArr.get(mid+1):
                if mountainArr.get(mid-1)>mountainArr.get(mid):
                    peak=mid-1
                else:
                    peak=mid
            else:
                if mountainArr.get(mid+1)>mountainArr.get(mid):
                    peak=mid+1
                else:
                    peak=mid

        left=0
        right=peak

        while left<=right:
            mid=(left+right)//2
            mid_val=mountainArr.get(mid)

            if mid_val==target:
                return mid

            if mid_val<target:
                left=mid+1
            else:
                right=mid-1   

        left=peak
        right=mountainArr.length()-1

        while left<=right:
            
            mid=(left+right)//2
            mid_val=mountainArr.get(mid)

            if mid_val==target:
                return mid

            if mid_val<target:
                right=mid-1
            else:
                left=mid+1   

        return -1         
        