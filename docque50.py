def str():
    i=0
    l=[]
    while i<len(a):
        j=0
        while j<len(a[i][j]):
            l.append(a[i][j])
        
        i=i+1
    print(l)
a=(input("enter"))
str()