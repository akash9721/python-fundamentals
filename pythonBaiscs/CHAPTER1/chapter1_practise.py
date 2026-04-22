
# task 1
# print multiline intro

print('''hello, my name is akash, 
i am from up
but currently i am living in delhi,
and i am software engineer''')

print() # task 2
# install external module and use it

# installing external module using pip like       => pip install numpy
import numpy as np
arr=np.array([1,2,3,4,5])

plus5=arr+5
square=arr**2

print("array", arr)
print("plus 5 arrays elements ",plus5)
print("square of each element ",square)

print() # task 3
# list all files present in a directory
import os
directory_path="/"
content = os.listdir(directory_path)
for items in content:
    print(items)
