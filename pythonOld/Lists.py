list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i , end=' ')

print()
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
list1.sort(reverse=True)
print(list1)

sum = 0
for i in list1:
    sum+=i
print(sum)

# list indexing
print("\n List indexing: ")
list2=[1,2,3,4,5,6,7,8,9,10]
print(list2[1:4])
print(list2[:])
print(list2[0])
print(list2[0::2])
print("reverse of list")
print(list2[-1])

print("\n Some operation for list")
list2.append(111);
print(list2)
list2.insert(6 , 55)
print(list2)

# check whether element is exisits or not
print("\n check whether element is exisits or not")
print(0 in list2)

list2.clear()
print(list2)

# extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
