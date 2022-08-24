fp = open(r"/home/rudnesh/Desktop/school/text2.txt",'r+')
a=fp.readlines()
newfp=open(r"/home/rudnesh/Desktop/school/newtext.txt",'a')
for i in range(len(a)):
    if "a" not in a[i]:
        print(a[i])
        newfp.write(a[i])
fp.close()
    