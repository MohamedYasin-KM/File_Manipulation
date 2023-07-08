#importing required modules
import sys
import csv

#creating list of items
details = [["Yasin","Developer"],["Sam","Tester"],["Roshan","Specialist"],["Vijay","Actor"],["Ajith","Actor"]]

#creating empty dictionary
dic = {}

#iterating over list and adding the values in the dictionary
for name,dept in details:
    dic[name] = dept
print(dic)

def text_file(filename):
    with open(filename,'w') as file: #open the file in write mode
        for name,dept in dic.items(): #iterating over dictionary
            write = file.writelines("{} is a {} \n".format(name,dept)) #written the data  in the file

def csv_file(filename):
    with open(filename,'w') as file: #open the file in write mode
        fieldnames = ["Name","Dept"] #mentioning fieldnames
        writer = csv.DictWriter(file,fieldnames=fieldnames)  
        writer.writeheader() #write the header
        for name,dept in dic.items():
            writer.writerow({"Name":name,"Dept":dept})


user_input = int(input("Enter a number : "))
if user_input==1:
    text_file('report.txt')
elif user_input==2:
    csv_file('report.csv')
else:
    sys.exit("Please Enter 1 or 2")


