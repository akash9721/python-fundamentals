str = "Akash Kumar"

# length of string
print("length of string is", len(str))

print(str.startswith("ak"))
print(str.endswith("ar"))

# strip() and replace(): strip() removes leading and trailing whitespace from the string
print()
demo = " to many space   "
print(demo.strip())
print(str.replace("kumar","gaur"))

# upper lower
print()
print(str.upper())
print(str.lower())

# Concatenating and Repeating Strings
print()
s1 = "hello "
s2 = "world"
result = s1+s2
print(result)
# repeat a string multiple times using * operator.
print(s1* 3)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# f string
print()
name = "akash"
age = "27"
company = "CDOT"
print(f"""My name is {name},
my age is {age} and 
i worked in {company}""")

print()
print(f"five times ten is {5*10}")
print(f"name in upper case is {name.upper()}")

pi = 3.14159265
print(f"Pi to 2 decimal places: {pi:.2f}")
# 'Pi to 2 decimal places: 3.14'

salary = 1000000
print(f"Formatted salary: ${salary:,}")

# Adding an equals sign automatically prints the variable name and its value. This is a massive timesaver for debugging
print()
x=10
y=20
print(f"value of x is {x} and value of y is {y=}")

# in keyword checks if a particular substring is present in a string.
print()
s = "akashkumar"
print("kumar" in s)

