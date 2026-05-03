s = "aafbbcddee"

fre = {}

for ch in s:
    fre[ch]=fre.get(ch,0)+1

for k,v in fre.items():
    if v==1:
        print(k)
        break

#####################################
print()
s = "aafbbcddee"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break