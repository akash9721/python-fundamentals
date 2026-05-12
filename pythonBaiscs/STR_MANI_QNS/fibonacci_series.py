a,b=0,1
print(a,end=" ")
print(b,end=" ")
for i in range(1,10):
    c=a+b
    print(c,end=" ")
    a=b
    b=c


################################################
print()
print("using recursion")
def fibbo_series(n):
    if n<=1:
        return n
    return fibbo_series(n-1)+fibbo_series(n-2)


for i in range(0,5):
    print(fibbo_series(i),end=" ")


