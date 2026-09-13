class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i=0
        j=len(people)-1
        count=0

        if people[-1]>limit:
            return -1

        while i<j:
            if people[j]+people[i]<=limit:
                i+=1
                j-=1
                count+=1
            else:
                j-=1
                count+=1
        
        if i==j:
            count+=1
        
        return count