user ={
    "name":"akash",
    "age":27,
    "company":"CDOT",
    "location":"delhi",
    "yoe":3
}

# accessing
for key,value in user.items():
    print(f"{key} : {value}")

print()
print(user.items())

print()
print(user.keys())

print()
print(user.values())

# adding updating
print()
user.update({"yoe":4})
print(user)