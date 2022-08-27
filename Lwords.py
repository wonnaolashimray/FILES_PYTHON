f=open("Lwords.txt","r")
x=f.read().split()
i=0
max=x[i]
while i<len(x):
    if len(x[i])>len(max):
        max=x[i]
    i+=1
print(max)
f.close()
