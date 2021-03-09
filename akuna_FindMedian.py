class Solution:

    def find_median(self, num_list, k):
        subarray = [i for i in num_list if i < k]


    def median_of_medians(self,A, i):

        #divide A into sublists of len 5
        sublists = [A[j:j+5] for j in range(0, len(A), 5)]
        medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians)/2]
        else:
            #the pivot is the median of the medians
            pivot = self.median_of_medians(medians, len(medians)/2)

        #partitioning step
        low = [j for j in A if j < pivot]
        high = [j for j in A if j > pivot]

        k = len(low)
        if i < k:
            return self.median_of_medians(low,i)
        elif i > k:
            return self.median_of_medians(high,i-k-1)
        else: #pivot = k
            return pivot

sol = Solution()
print(sol.find_median([1,2,3,4,5,6,7,8,9], 3))