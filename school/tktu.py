# !/usr/bin/python3  
from queue import Full
from tkinter import *  

p = Tk()
p.title("Media notes")
p.geometry("850x850")
p["background"]='#f8f8f8'
lb=Label(p,height=1,width=250,bg="#050509",pady=3).place(x=0,y=0)
b1=Button(p,width=5,bg="#050509",bd=0, 	
pady=0.1,text="File",fg="white",activebackground="#050509",activeforeground="white",borderwidth=0).place(bordermode="outside",x=2.3,y=2)
l2=Button(p,height=1,width=2,bg="#050509",bd=0,relief="flat",borderwidth=0,
pady=0.01,text="Edit",fg="white",activebackground="#050509",activeforeground="white").place(x=58,y=2,bordermode="outside")
p.mainloop()

