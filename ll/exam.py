a= [5,2,8,9]
b=[7,5,9,2,4]
j = 0
a.sort()
b.sort()
# print(a)
i,j=0,len(a)-1
count =0
while i<=j:
    
    if a[i]+a[j]<=b[i]:
        i+=1
        j=j-1
    j-=1
print(count)


