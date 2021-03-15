class Solution:

    def array_journey(self, path, k):
        if not path:
            return 0
        return self.helper(0, path,k, [])

    def helper(self, position,path,k, dict):
        if position in dict:
            return dict[position]
        new_score = -float('inf')
        for i in range(1,k+1):
            new_position = position + i
            if new_position >= len(path):
                break
            new_score = max(self.helper(new_position, path, k), new_score)
        result = path[position] if new_score == -float('inf') else path[position] + new_score
        dict[position] = result

        return result







sol = Solution()


path = []
k = 2


print(sol.array_journey(path, k))