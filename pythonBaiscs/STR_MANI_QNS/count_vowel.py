str = "akash kumar"

count = 0
for i in str:
    if i in "aeiou":
        count += 1
        print(i,end=",")

print(f"no of vowel is : {count}")