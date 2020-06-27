import kadaneMSS


#Kadane's w/ indices    
arr = [-9.0, 10.0, 2.0, 3.0]#[-10,9,2,4]
soln = kadaneMSS.MaxSubArrSum(in_arr=arr, size=len(arr))

print(soln.max_subarray_sum_with_indices.__doc__)
max_sum, lcur, rcur = soln.max_subarray_sum_with_indices()
print(arr[lcur:rcur], "sum:", max_sum)