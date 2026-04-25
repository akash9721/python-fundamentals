a = (1,45,342,4545,False,"Rohan","Shivam")

# task is update index value 1 a[0]=453

# convert it into list then change and again convert it into tuple
list=list(a)
list[0]=453
a=tuple(list)
print(a)

# count zero in tuple
print()

tup1 = (3,5,0,2,0,0,6,0)
n=len(tup1)
cnt=0
for i in range(n):
    if(tup1[i]==0):
        cnt+=1

print(f"no of zero is {cnt}")

