def LCS(arr):
    n=len(arr)
    lis=[1]*n
    for i in range(n):
        for j in range(i):
            if(arr[i]>arr[j]) and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1
    return max(lis)
print(LCS([1,2,3,4]))