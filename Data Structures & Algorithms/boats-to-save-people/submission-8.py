class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start=0
        end=len(people)-1
        count=0

        while people[end]+people[start]>limit and (start<=end):
                end=end-1           

        
        if end==-1:
            return len(people)
        else:
            count+=len(people)-1-end
        
        print(count)
        curr_limit=people[end]+people[start]
        
        while curr_limit<=limit and (start<end):
            count+=1
            start+=1
            end-=1
            print(count,start,end)
            curr_limit=people[end]+people[start]
        
        count+=end-start+1
        print(count,end,start)

        return count
        

        

        