# args examples
def sum_all(*args):
    return sum(args)


print(sum_all(5, 5, 5))
print(sum_all(4, 4, 4, 4))
print(sum_all(9, 9, 9, 9, 9))


def printLog(*args):
    print(args)


printLog("INFO")
printLog("INFO", "CRITICAL")
printLog("INFO", "CRITICAL", "ERROR")

################################kwargs example#######################
print()


def info(**kwarg):
    for k, v in kwarg.items():
        print(f"{k} : {v}")


info(name="akash", age=27, city="Delhi")

#########################################################################
print()


def catch_extra(first, *args):
    print(f"First: {first}")
    print(f"Extra Positional: {args}")


catch_extra("Apple", "Banana", "Cherry", "Date")


# "Apple" goes to 'first'
# ("Banana", "Cherry", "Date") are the Extra Positional Arguments


###########################################################################
# mix of normal,args,and kwargs
def mix_args(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i,end=" ")
    print()
    for k,v in kwargs.items():
        print(f"{k} : {v}")


mix_args("Hindi", 20, 60, Subject="Hindi", result="Pass")
