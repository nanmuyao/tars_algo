#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0,0] for i in range(len(prices))]
        dp[0][0] = -prices[0] # hold
        dp[0][1] = 0 #empty
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        return dp[len(prices) - 1][1]

空间优化：转移的时候，dp[i]dp[i] 只会从 dp[i-1]dp[i−1] 转移得来，因此第一维可以去掉：
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[] dp = new int[2];
        dp[0] = 0;
        dp[1] = -prices[0];
        for (int i = 1; i < n; i++) {
            int tmp = dp[0];
            dp[0] = Math.max(dp[0], dp[1] + prices[i]); 
            dp[1] = Math.max(dp[1], tmp - prices[i]);
        }
        return dp[0];
    }
}

