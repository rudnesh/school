fp=open(r"/home/rudnesh/Desktop/school/text.txt",'r')
m=fp.read()
a =m.split()
for i in a :
    print(i+"#",end="")
fp.close()