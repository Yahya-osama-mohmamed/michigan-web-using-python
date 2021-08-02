import re
numbers=[]
sum=0
name = input("Enter file:")
if len(name) < 1 : name = "a.txt"
handle = open(name)
for line in handle:
 line=line.rstrip()
 

 numbers=numbers+re.findall('[0-9]+',line)
 
for num in numbers:
    sum=sum+int(num)



print (sum)