class StockSpanner:

    def __init__(self):
        self.monotonic_stack=[(1e10,0)]
        self.curr_day=0

    def next(self, price: int) -> int:
        while self.monotonic_stack and price>=self.monotonic_stack[-1][0]:
            _,pos=self.monotonic_stack.pop()
        
        self.curr_day+=1
        self.monotonic_stack.append((price,self.curr_day))
        return self.curr_day-self.monotonic_stack[-2][1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)