def fun(fname):
    with open(fname)as f:
        g=f.read().split()
        i=0
        c1=0
        c2=0
        while i<len(g):
            j=0
            while j<len(g[i]):
                if g[i][j]=="A" or g[i][j]=="a":
                    c1+=1
                if g[i][j]=="M" or g[i][j]=="m":
                    c2+=1
                j+=1
            i+=1
        print("A or a=",c1)
        print("M or m=",c2)
fun("story2.txt")        

# f=open("story2.txt","r")
# count=0
# count1=0
# c=f.read()
# d=c.split()
# i=0
# while i<len(d):
#     j=0
#     while j<len(d[i]):
#         if d[i][j]=="a" or d[i][j]=="A":
#             count+=1
#         if d[i][j]=="m" or d[i][j]=="M":
#             count1+=1
#         j+=1
#     i+=1
# print("A or a=",count)
# print("M or m=",count1)
# f.close()
