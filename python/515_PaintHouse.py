class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        if not costs:
            return 0
        # write your code here
        return self.helper(costs,0,None, {})

    def helper(self, costs, position, previous, dict):
        if (position, previous) in dict:
            return dict[(position, previous)]
        total_cost = float('inf')
        for i in range(3):
            if previous is not None:
                if i == previous:
                    continue
            if position+1 == len(costs):
                total_cost = min(total_cost, costs[position][i])
            else:
                total_cost = min(total_cost, costs[position][i] + self.helper(costs,position+1, i,dict))
        dict[(position, previous)] = total_cost
        return total_cost

sol = Solution()
cost = [[1,2,3],[1,4,6]]
print(sol.minCost(cost))


