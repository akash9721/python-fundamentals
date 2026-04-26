# task 1 : find greatest of four no enter by user in python
number = []
n = int(input("enter a no "))
for i in range(n):
    no = int(input(f"enter {i+1} no "))
    number.append(no)

max_ele=number[0]
for i in number:
    if(i>max_ele):
        max_ele=i

print(f"maximum of 4 no is : {max_ele}")


# task 2 : write a program to check whether a post is talking abut "akash" or not

post = input("enter a post line ")

if("akash" in post.lower()):
    print(f"Yes this post is taking about akash")
else:
    print(f"No this post is not talking about akash")
