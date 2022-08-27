f=open("ing_file.txt","r")
count=0
a=f.read()
b=a.split()
for i in b:
    if "ing" in i:
        count+=1
print(count)