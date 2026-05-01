# write a program to find factorial
def findFactorial(n):
    if(n==0 or n==1):
        return 1
    return n*findFactorial(n-1);

n = int(input(f"enter a no : "))
factorial=findFactorial(n)
print(f"factorial of {n} is {factorial}")