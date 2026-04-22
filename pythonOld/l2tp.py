import random

list=[]

def insertImsiNo():
    n = input("enter a no ")
    for i in range(int(n)):
        list.append(str(random.randint(9958000000, 9958999999)))
    print(list)

def deleteImsiNo():
    global list
    list.reverse()
    m = input("enter range for deletion ")
    for i in range(int(m)):
        list.pop()
    print(list)

insertImsiNo()
deleteImsiNo()

