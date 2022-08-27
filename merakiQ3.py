f=open("merakiQ3.txt","r")
delhi=open("delhi.txt","w")
jaipur=open("jaipur.txt","w")
shimla=open("shimla.txt","w")
cochin=open("cochin.txt","w")
x=f.readlines()
print(x)
i=0
while i<len(x):
    if "delhi"in x[i]:
        delhi.write(x[i])
    elif "jaipur"in x[i]:
        jaipur.write(x[i])
    elif "shimla"in x[i]:
        shimla.write(x[i])
    elif "cochin"in x[i]:
        cochin.write(x[i])
    i+=1
f.close()       
