lower=0
upper=0
f=open("lower_case.txt","r")
line=f.read()
for i in line:
    if i.islower()==True:
        lower+=1
    elif i.isupper()==True:
        upper+=1
print("total no.of lower_case=",lower)
print("total no. of upper_case=",upper)