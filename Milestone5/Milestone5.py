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
count2=len(lstind)

file4=open('Milestone5.txt', 'w')
file3=open('Source.txt')
boundary=''
layer=''
datatype=''
xy=''

for line in file3:
    lst1=''
    lstspare1=[]
    x1,y1=[],[]
    lstind1=[]
    res=[]
    res1=[]
    if line.startswith("boundary"):
        boundary=line
    elif line.startswith("layer"):
        layer=line
    elif line.startswith("datatype"):
        datatype=line
    elif line.startswith("xy"):
        xy=line
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
        if len(x1)==len(x) and len(y1)==len(y):
            for i in range(len(x)):
                xo=x[i]
                xt=x1[i]
                yo=y[i]
                yt=y1[i]
                p=round(((((xt - xo)*2) + ((yt-yo)**2) )*0.5))
                res.append(p)
        res1 = res
        if res==res1:
            file4.writelines(boundary)
            file4.writelines(layer)
            file4.writelines(datatype)
            file4.writelines(xy)
            file4.writelines("endel\n")
        del boundary
        del layer
        del datatype
        del xy