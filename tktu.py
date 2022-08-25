from tkinter import *
p = Tk()
p.title("Media notes")
menubar = Menu(p,background="#050509")
filemenu = Menu(menubar, tearoff=0,activeforeground="#837f7f",fg="white",background= "#050509")

filemenu.add_command(label="New",activebackground="#050509",activeforeground="white",command=None)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Save as...", command=None)
filemenu.add_command(label="Close", command=None)

filemenu.add_separator()

menubar.add_cascade(label="File",foreground = 'white' , menu=filemenu)
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/menu-coptions.html
p.config(menu=menubar)
p.mainloop()