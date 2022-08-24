a=int(input("enter the number: "))
odd=0
even=0
for i in range(a):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("odd number",odd)
print("even number",even)
