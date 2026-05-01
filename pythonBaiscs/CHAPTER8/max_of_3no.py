# find greatest of 3 no
def threeMaximumNo(list):
    n = len(list)
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    for ele in list:
        if ele > first:
            third = second
            second = first
            first = ele
        elif ele > second :
            third = second
            second = ele
        else:
            ele = third

    return first, second, third


arrlist = [5, 9, 3, 45, 2, 11, 65, 0]
first,second,third=threeMaximumNo(arrlist)
print(f"3 maximum no is : {first} ,{ second} , {third}")

# using predefine method
data = sorted(arrlist, reverse=True)
print(f"sorted data using predefie function : {data}")
max_3data = sorted(arrlist, reverse=True)[:3]
print(f"sorted data using predefie function : {max_3data}")
