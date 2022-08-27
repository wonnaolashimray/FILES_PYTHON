# f=open("wonnao.jpeg","rb")
# x=f.read()
# print(x)


f=open("wonnao.jpeg","rb")
f1=open("my_pic.jpeg","wb")
for i in f:
    f1.write(i)
f.close()


