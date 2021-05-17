class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        if not numbers:
            return []
        if len(numbers) < 3:
            return []

        numbers.sort()

        num_dict = {}
        result = set()
        for n in numbers:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1

        for i in range(len(numbers)):
            a = numbers[i]
            num_dict[a] -= 1
            for j in range(i, len(numbers)):
                b = numbers[j]
                if num_dict[b] <= 0:
                    continue
                c = -a -b
                num_dict[b] -= 1
                if c in num_dict:
                    if num_dict[c]>=1:
                        temp = [a,b,c]
                        temp.sort()
                        result.add(tuple(temp))
                num_dict[b] += 1
            num_dict[a] += 1

        return result

numbers = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(numbers))
