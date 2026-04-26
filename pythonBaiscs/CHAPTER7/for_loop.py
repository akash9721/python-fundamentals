# example 1

price = [90,60,80,70,95]
discount_price = []

for ele in price:
    discount = ele* 0.9
    discount_price.append(discount)

print(f"without discount price are {price}")
print(f"new discount prices are {discount_price}")

print()

# example 2 iterate over dictionary
user = {
    "name": "akash",
    "age": 27,
    "company": "PHONEPAY",
    "position": "SRE",
    "salary": "16LPA+"
}

print(f"user data is ")
for key,value in user.items():
    print(f"{key} -> {value}")