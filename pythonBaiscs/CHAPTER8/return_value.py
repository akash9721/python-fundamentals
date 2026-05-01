# with return value and with argument
def findMax(arr, n):
    first = 0;
    second = 0;
    for i in arr:
        if i > first:
            second = first;
            first = i
        elif i > second and i != first:
            second = i

    return first, second


#    print(f"first and second maxmum element are :=== first : {first} ___ second : {second}")

arr = [3, 6, 2, 8, 22, 7]
max1, max2 = findMax(arr, len(arr))
print(f"first and second maxmum element are :=== first : {max1} ___ second : {max2}")



###################################################################################################
def operations(list):
    return min(list),max(list),sum(list),sum(list)/len(list)


low,high,all,average = operations([5, 2, 3, 10, 6, 4, 0])
print(f"{low} {high} {all} {average:.2f}")
