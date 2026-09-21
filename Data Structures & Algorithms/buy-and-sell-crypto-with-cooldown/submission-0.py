class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # At each day, I can have 2 choices: I can either buy or I can either sell
        # I can do as many transactions as I like
        # If I sell, I'll need to know my buying price previously and then I can recursively call some maxProfit function for an element next to me right now
        # If I buy, I can just record that information and then move on to call the next element in the array
        # I'll need to see what time I'll need to sell, like when do we decide when to sell
        # Can we do this? For each step, I'll buy it and then call maxProfit to a smaller instance and I also sell it, record the profit and call maxProfit, whichever gives me more profit I go with that approach? This seems like a promising approach. Do I need to try out all of the cases at all times and return the best case? So for every case, what you do is
        # dp[i] = max profit starting from i-th day
        # dp[i] = max(prices[i] - prices[j] + dp[j + 2]) for j till the array's length
        # For a bottom-up dynamic programming, we start from the right most element and then build up our solution from there.
        # if prices[i] - prices[j] < 0, we can immediately ignore that as it is not possible to 
        # make a good profit in that case? Althogh it might naturally be ignored anyway.
        n = len(prices)
        dp = [0] * (n + 2)   

        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1]              # option: skip day i entirely
            day_a = prices[i]
            for j in range(i+1, n):
                day_b = prices[j]
                profit = day_b - day_a
                dp[i] = max(dp[i], profit + dp[j+2])

        return dp[0]       

