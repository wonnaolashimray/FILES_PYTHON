f=open("story.txt","r")
x=f.read().split()
i=0
c1=0
c2=0
while i<len(x):
    if x[i]=="Me" or x[i]=="me":
        c1+=1
    if x[i]=="My":
        c2+=1
    i+=1
print("Me=",c1)
print("My=",c2)
f.close()