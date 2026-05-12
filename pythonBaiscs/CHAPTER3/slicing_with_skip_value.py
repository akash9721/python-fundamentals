str = "namesapace"

# a string using [start:stop:step].
print(str[1:10:3])

# without stop condition
text = "abcdefghijk"
# Indices:
# a = 0
# b = 1 (Start)
# c = 2
# d = 3
# e = 4 (Step 3 from 'b')
# f = 5
# g = 6
# h = 7 (Step 3 from 'e')
# i = 8
# j = 9
# k = 10 (Step 3 from 'h')

#text = "abcdefghijk"
print(text[1::3])  # 'behk'

#some extra
text = "Python"
print(text[::2])  # 'Pto' (Indices 0, 2, 4)

text = "Python"
print(text[::-1])  # 'nohtyP'

text = "Python"
print(text[::-2])  # 'nhy' (Indices -1, -3, -5)

text = "Python"
print(text[2::])  # 'thon' (Indices 2 to the end)

text = "Python"
print(text[1::2])  # 'yhn' (Indices 1, 3, 5)