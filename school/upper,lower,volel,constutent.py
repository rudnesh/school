


vowel="A"," E"," I", "O", "U","a","e","i","o","u"
consonants =["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","z"]
fp=open(r"/home/rudnesh/Desktop/school/text.txt",'r')
cvowel= 0
cconsonants=0
up=0
lo=0
m=fp.read()
a=list(m)
for i in range(len(a)) :
    if(m[i]=='a' or m[i]=='e' or m[i]=='i' or m[i]=='o' or m[i]=='u' or m[i]=='A' or m[i]=='E' or m[i]=='I' or m[i]=='O' or m[i]=='U'):
        cvowel=cvowel+1
    elif(m[i]=='B' or m[i]=='C' or m[i]=='D' or m[i]=='F' or m[i]=='G' or m[i]=='H' or m[i]=='J' or m[i]=='L' or m[i]=='M' or m[i]=='N'or m[i]=='P' or m[i]=="Q" or m[i]=='R' or m[i]=='S' or m[i]=='T' or m[i]=='v' or m[i]=='z' or m[i]=='x' or  m[i]=='b' or m[i]=='c' or m[i]=='d' or m[i]=='f' or m[i]=='g' or m[i]=='h' or m[i]=='j' or m[i]=='l' or m[i]=='m' or m[i]=='n' or m[i]=='p' or m[i]=="q" or m[i]=='r' or m[i]=='s' or m[i]=='t' or m[i]=='v' or m[i]=='z' or m[i]=='x'):
        cconsonants=cconsonants+1
    elif m[i].isupper():
        up=up+1
    elif m[i].lower():
        lo=lo+1
print(cvowel,up,lo,len(a),up+lo,cconsonants)

