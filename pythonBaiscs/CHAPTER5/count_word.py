str = "akash kumar"
print(str[::-1])

#####################################################
print()
list=["akash","nandu","krishna","akash","nandu"]

freq={}

for ele in list:
    freq[ele]=freq.get(ele,0)+1


print(freq)

#####################################################
print()
text = "apple banana apple orange banana apple"
wordCount={}
for word in text.split():
    wordCount[word]=wordCount.get(word,0)+1


print(wordCount)