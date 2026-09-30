class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
           # Okay, this is about picking a subsequence, with unlimited repetition. So, it's an unbounded knapsack problem pattern. 
           # Let dp[i][a] define the number of combinations that makes up amount a with index upto i. 
           # If I choose to take the current item, then I'll need to see if I can make the rest of the amount using the coins I have upto that index.
           # If I choose to not take the current item, then I'll need to see if I can make the current amount excluding that specific index.
           # I'll need to add them together and get the number.
           # For bottom up, I need [0][0] first before I can process anything else. I can set the base cases to 1 and move on with my choices.

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i + 1][a]              # skip coins[i]
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]  # take coins[i]

        return dp[0][amount]