# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
a=tk.Tk()
a1=tk.Label(a,text='Calculator',font='Bell 20',fg='red',bg='blue')
a1.grid(row=0,column=5,padx=150,pady=10)
sa1=tk.Scrollbar()
listbox1=tk.Listbox()
def Button_back():
    b2.grid_forget()
    b1.grid(row=1,column=1)
    ba1.grid(row=2,column=1)
    ba2.grid(row=2,column=2)
    ca2.grid_forget()
    ca1.grid_forget()
b2=tk.Button(a,text='settings',fg='red',height=5,width=10,command=Button_back)
def Button_settings():
    b2.grid(row=1,column=4,pady=5)
    b1.grid_forget()
    ba1.grid_forget()
    ba2.grid_forget()
def color_red():
    pass
b1=tk.Button(a,text='back',fg='red',height=5,width=10,command=Button_settings)
ca1=tk.Button(a,bg='red',command=color_red,height=5,width=10)
def Button_back1():
    b1.grid(row=1,column=1)
    ba2.grid(row=2,column=1)
    ba2.grid(row=2,column=2)
ca2=tk.Button(a,text='Back',bg='white',fg='black',height=5,width=10,command=Button_back)
def Button_color():
    b1.grid_forget()
    ba1.grid_forget()
    ba2.grid_forget()
    ca2.grid(row=1,column=1)
    ca1.grid(row=2,column=1)
ba1=tk.Button(a,text='color',fg='black',bg='white',height=5,width=10,command=Button_color)
ba2=tk.Button(a,text='font',fg='red',bg='green',height=5,width=10)
def Button_font():
    pass
Button_settings()
a.mainloop() 