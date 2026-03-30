class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo=[-1 for i in range(amount+1)]
        self.min_denom=min(coins)
        self.max_amount=amount

        def coinChange_memo(amount):
            if amount==0:
                self.memo[0]=0
                return 0
            elif amount<self.min_denom:
                return self.max_amount+1 
            if self.memo[amount]!=-1:
                return self.memo[amount]
            else:
                true_amount=amount+1
                for coin in coins:
                    true_amount=min(true_amount,1+coinChange_memo(amount-coin))
                self.memo[amount]=true_amount
                return self.memo[amount]
        
        coinChange_memo(amount)
        if self.memo[amount]>amount:
            return -1
        return self.memo[amount]
        