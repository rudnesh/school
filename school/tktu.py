from tkinter import *
from tkinter import colorchooser as color
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
p = Tk()
p.title("Media notes")
p.geometry("1000x500")
def choose_color():
    # variable to store hexadecimal code of color
    color_code = color.askcolor(title ="Choose color")
    p["background"]=list(color_code[1:2])
clicks = 0
a=[]
tex=[]
class textbox:
    def area():     
        global p ,a,y,box,tex
        global clicks #this will use the variable to count
        clicks =+ 1
        n=[]
        a.append(n)
        y=len(a)
        for x in range(clicks):
            box=Text(p,height=10,width=100)
            n.append(box)
            n[x].pack(padx=10,pady=20)
            
    def newfile():
        filetypes = (
        ('text files', '*.py'),
        ('All files', '*.*'))
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        print(filename)
    def save():
        
        for row in range(len(a)):
            for col in range(clicks):
                r=a[row][col].get(1.0,END)
                tex.append(r)
                print(len(a))
    def save_file():
        f = asksaveasfile(initialfile = 'Untitled.txt',
            defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
menubar = Menu(p,background="#050509")
filemenu = Menu(menubar, tearoff=0,activeforeground="#837f7f",fg="white",background= "#050509")
filemenu.add_command(label="New file",activebackground="#050509",activeforeground="white",command=textbox.newfile)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=lambda: textbox.save())
Button(p, text='newbox', command= textbox.area).place(x=1535)
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
p.pack_slaves()
p.mainloop()
print(tex)