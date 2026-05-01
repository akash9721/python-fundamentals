sqare = lambda x:x*x
print(sqare(5))


# map
nums = [1, 5, 8, 10, 13]

# multiply 2 of each ele
update = map(lambda x: x * 2, nums)
print(list(update))

# filter
print()
# Keep only even numbers
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))

# sorted
print()
# sort in ascending order
sorted(nums)

#############################################
print()
scores = {"Rahul": 45, "Amit": 88, "Sonia": 32, "Priya": 91}

sort_by_value = sorted(scores.items(), key=lambda x: x[1])
print(dict(sort_by_value))
top_scorers = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(dict(top_scorers))
sort_by_key = sorted(scores.items(), key=lambda x: x[0])
print(dict(sort_by_key))
