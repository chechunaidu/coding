def LCIS(arr1,n,arr2,m):
    table=[0]*m

    for i in range(n):
        current=0
        for j in range(m):
            if(arr1[i]==arr2[j]):
                if(current+1>table[j]):
                    table[j]=current+1
            if arr1[i]>arr2[j]:
                if(table[j]>current):
                    current=table[j]
    for i in range(m-1):
        if table[i]>table[i+1]:
            print(arr2[i])

    return max(table)
 

l1=[3,4,9,1]
n=len(l1)
l2=[5,3,8,9,10,2,1]
m=len(l2)
print(LCIS(l1,n,l2,m))