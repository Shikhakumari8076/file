f=open("pep.txt","r")
data=f.read()
f.close()
print(data)
i=0
c=0
while i<len(data):
    if data[i]=="\n":
        c=c+1
    i=i+1
print(c)