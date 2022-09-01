from tkinter import  *

root = Tk()
n_array = []        #will be used as 2d array

def add_four_entries():
    global root, n_array

    row_array=[]    #array used to store a row
    n_array.append(row_array)
    y=print(len(n_array))
	          

    for x in range(4):
        tbn=Text(root)
        row_array.append(tbn)
        row_array[x].grid(row=y, column=x,sticky="nsew", padx=2,pady=2)

def getval():
    for row in range(len(n_array)):

        for col in range(4):
              n_array[row][col].get(1.0,END) ,print(col)
			 

            
Button(root, text="Add new row", command=add_four_entries).grid(row=0, column=1,)
Button(root, text="Print val", command=getval).grid(row=21, column=1,)
mainloop()