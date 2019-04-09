list1=[[1,2,3],[1,2,3],[1,2,3]]
row=len(list1[0])
columns=len(list1)
result=[[0 for i in range(row)]for i in range(columns)]
for i in range(row):
    for j in range(columns):
        result[i][j]=list1[j][i]
print(result)