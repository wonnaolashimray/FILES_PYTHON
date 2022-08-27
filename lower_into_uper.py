f=open("lower_into_upper.txt","r")
x=f.read()
a=""
b=[]
i=0
while i<len(x):
    if x[i]>="A" and x[i]<="Z":
        d=x[i].lower()
        a+=d
    else:
        c=x[i].upper()
        a+=c
    i+=1
j=0
while j<len(a):
    if a[j]>="A" and a[j]<="Z":
        b.append(j)
    j+=1
print(a)
print(b)
f.close()