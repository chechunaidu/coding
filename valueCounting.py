items=["apple","pear","orange","apple","orange","apple","orange","pear"]

fruits=dict()

for key in items:
    if(key in fruits.keys()):
        fruits[key]+=1
    else:
        fruits[key]=1
    
print(fruits)
