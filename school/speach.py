from tkinter import *
from turtle import bgcolor
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0,activeforeground="white",fg="white" )

filemenu.add_command(label="New",activebackground="#050509",activeforeground="white",command=None)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Save as...", command=None)
filemenu.add_command(label="Close", command=None)

filemenu.add_separator()

menubar.add_cascade(label="File",activebackground = 'white' , menu=filemenu)


root.config(menu=menubar)
root.mainloop()