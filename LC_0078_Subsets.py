import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def num_to_binary_list(n, k):
            # generate list in form of binary representation of n of size k
            bin_repr, i = [False]*k, k-1
            while n > 0:
                bin_repr[i] = n%2 == 1
                n, i = n//2, i-1
            return bin_repr
        k = len(nums)
        bin_list = []
        # Generate list of all numbers in binary, binary repr in a list format
        for n in range(2**k):
            bin_list.append(num_to_binary_list(n, k))
        # Result is A[bin_repr]
        result = [list(compress(nums, bin_repr)) for bin_repr in bin_list]
        return result
