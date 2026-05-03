s = "programming"

seen = set()

for i in s:
    if i in seen:
        print(i,end=" ")
    seen.add(i)