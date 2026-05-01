str = "hey akash you are preparing SRE interview"
str2 = "\nthis is new line added"

text_io = open("myfile.txt", "w")
text_io.write(str)
text_io.write(str2)
text_io.close()




###################################################
# each time run each time add content at end
print()
list = ["First line\n", "Second line\n", "Third line\n"]
list2 = ["fourth line\n", "fifth line\n", "sixth line\n"]
with open("file3.txt","a") as file:
    file.writelines(list)
    file.writelines(list2)