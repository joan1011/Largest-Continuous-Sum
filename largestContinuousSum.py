def largestContinuousSum(arr):
    if len(arr)==0:
        return
    maxSum=currentSum=arr[0]
    for num in arr[1:]:
        currentSum=max(currentSum+num, num)
        maxSum=max(currentSum, maxSum)
    return maxSum
    
largestContinuousSum([8,10,-18,-20,-50,100])
