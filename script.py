import os
path = '/home/mohamed-yasin/Python Programs'
os.chdir(path)
os.path.join(path,'novel.txt')

with open('novel.txt','w') as file:
	file = file.write('The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality.')
with open('novel.txt','r')as file:
	file = file.read()
print(file)
