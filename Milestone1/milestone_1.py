file1=open("Format_Source.txt")
ctr = 0
with open ('milestone1.txt', 'w') as file:
    for line in file1:  
        if line.startswith("boundary") or line.startswith("layer") or line.startswith("datatype") or line.startswith("xy"):
            file.writelines(line)
        elif line.startswith("endel"):
            file.writelines(line)
            ctr=ctr+1
        if ctr==2:
            break
file.close()