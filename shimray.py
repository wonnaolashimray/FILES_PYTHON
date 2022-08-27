f=open("shim.txt","r")
x=f.readlines()
print(x)
count=0
for i in x:
    count+=1
print(count)
f.close()

