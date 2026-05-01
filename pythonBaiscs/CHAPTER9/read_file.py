# this will load all file at once
# also we need to close

f = open("file1.txt","r")
f_read = f.read()
print(f_read)
f.close()

# with is a context manager
# closed file automatically even if exception occur
with open("file1.txt", "r") as file:
    file_read = file.read()

with open("file1.txt", "r") as file:
    file_read2 = file.readline()

with open("file1.txt", "r") as file:
    file_read3 = file.readlines()

print(file_read) # print as written in file
print()
print(file_read2)  # read first line only
print()
print(file_read3) # read all line in a single line

# best for large file
print()
with open("file1.txt", "r") as file:
    for line in file:
        print(line.strip())