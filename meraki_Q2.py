bank=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("bank.txt","w")
for i in bank:
    f.write(i)
    f.write("\n")
f.close()

