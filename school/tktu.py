from tkinter import *
from tkinter import colorchooser as color
p = Tk()
p.title("Media notes")
def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = color.askcolor(title ="Choose color")
    p["background"]=list(color_code[1:2])

menubar = Menu(p,background="#050509")
filemenu = Menu(menubar, tearoff=0,activeforeground="#837f7f",fg="white",background= "#050509")

filemenu.add_command(label="New",activebackground="#050509",activeforeground="white",command=None)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Save as...", command=None)
filemenu.add_command(label="Close", command= lambda: p.quit())

filemenu.add_separator()
menubar.add_cascade(label="File",foreground = 'white' , menu=filemenu)
editmenu = Menu(menubar, tearoff=0,activeforeground="#837f7f",fg="white",background= "#050509")
editmenu.add_command(label="bgcolour",activebackground="#050509",activeforeground="white",command=choose_color)
editmenu.add_command(label="remove", command=None)
editmenu.add_command(label="size", command=None)
menubar.add_cascade(label="Edit",foreground = 'white' , menu=editmenu)
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/menu-coptions.html
p.config(menu=menubar)
p.mainloop()