import math

class MaxSubArrSum:
    def __init__(self, in_arr, size):
        self.in_arr = in_arr
        self.size   = size

        # if all items are positive,
        # solution is trivial: The main array!
        all_postive = True
        for idx in range(0, size):
            if in_arr[idx] < 0:
                all_postive = False
                break
        if all_postive is True:
            raise("All Inputs are Positive!")
    
    def max_subarray_sum_with_indices(self):
        """ Kadane's w/ inices
        Computes the subarray indices as well as maximum sum as well

        - Same as Kladane
            + find MSS until cur idx
            + collect the best
        - Note: How indices are caught

        TIME        : O(n)
        SPACE       : O(n)
        """
        MSS = -math.inf
        L_CUR = R_CUR = None
        _running_sum = 0

        for idx, val in enumerate(self.in_arr):
            # i. find max of sum-of-subarray that ends at `idx`
            if _running_sum <= 0:
                _running_sum  = val
                _start        = idx
            else:
                _running_sum += val

            # ii. collect best
            if _running_sum > MSS:
                MSS     = _running_sum
                L_CUR   = _start         
                R_CUR   = idx + 1

        # as idx starts and ends (beg, end) --
        # R_CUR should be inclusive in main driver code
        return MSS, L_CUR, R_CUR
