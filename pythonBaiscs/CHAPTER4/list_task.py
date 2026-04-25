#
fruits = []
n = int(input("enter no : "))
for i in range(n):
    fruit=input(f"fruit {i+1} ")
    fruits.append(fruit)

print(fruits)

# accept mark of 6 student display in sort
print()
marks = []
n = int(input("enter student count : "))
for i in range(n):
    mark=int(input(f"{i+1} student mark "))
    marks.append(mark)

print(sorted(marks))


# sum of 4 number
print()
list = [3,5,7,1]
n= len(list)
sum=0
for i in range(n):
    sum+=list[i]

print(f"sum is {sum}")
