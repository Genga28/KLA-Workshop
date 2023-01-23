file2=open('POI.txt')
lst=''
lstspare=[]
x,y=[],[]
for line in file2:
    
    if line.startswith("xy"):
        lst=line.split(' ')
        while("" in lst):
            lst.remove("") 
for i in range(2, len(lst)):
    lstspare.append(lst[i])
res = [eval(i) for i in lstspare]
for i in range(len(res)):
    if i%2==0:
        x.append(res[i])
    else:
        y.append(res[i]) 
lstind=[]
for i in range(len(x)):
    lstind.append((x[i],y[i]))
print(lstind)

file4=open('text.txt', "w")
file3=open('Source.txt')
for line in file3:
    boundary=''
    layer=''
    datatype=''
    xy=''
    lst1=''
    lstspare1=[]
    x1,y1=[],[]
    lstind1=[]
    if line.startswith("boundary"):
        boundary=line
    elif line.startswith("layer"):
        layer=line
    elif line.startswith("datatype"):
        datatype=line
    elif line.startswith("xy"):
        xy=''
        lst1=line.split(' ')
        while("" in lst1):
            lst1.remove("") 
        for i in range(2, len(lst1)):
            lstspare1.append(lst1[i])
        res1 = [eval(i) for i in lstspare1]
        for i in range(len(res1)):
            if i%2==0:
                x1.append(res1[i])
            else:
                y1.append(res1[i]) 
        for i in range(len(x1)):
            lstind1.append((x1[i],y1[i]))
        for i in lstind:
            for j in lstind1:
                if i==j:
                    file4.writelines(boundary)
                    file4.writelines(layer)
                    file4.writelines(datatype)
                    file4.writelines(xy)