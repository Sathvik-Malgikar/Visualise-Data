from ctypes import alignment
import string
from tkinter import *
from tokenize import String

from numpy import size

root=Tk()
# root.resizable(0)
root.title('Simple Calulator')
root.geometry("400x500")
memory=StringVar(root) 
memory.set(0) 
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=3)
# root.configure(colbgour='grey')
disp_e=Entry(root,textvariable=memory,relief=RAISED,borderwidth=3,font=('Helvetica',26),width=12)
disp_e.grid(row=0,padx=10,pady=3)

f1=Frame(root,background='grey',width=380,height=300)
f1.grid(row=1,column=0,sticky=W,padx=10,pady=7)

def add(w):

    t=memory.get()
    if t=='0':
        t=''
    memory.set(t+str(w))



b7=Button(f1,text=7,font=('Helvetica',17),command= lambda : add(7)  )
b7.place(x=30,y=20)
b8=Button(f1,text=8,font=('Helvetica',17),command=lambda : add(8) )
b8.place(x=82,y=20)
b9=Button(f1,text=9,font=('Helvetica',17),command=lambda : add(9) )
b9.place(x=134,y=20)
b4=Button(f1,text=4,font=('Helvetica',17),command=lambda *args : add(4) )
b4.place(x=30,y=85)
b5=Button(f1,text=5,font=('Helvetica',17),command=lambda *args : add(5) )
b5.place(x=82,y=85)
b6=Button(f1,text=6,font=('Helvetica',17),command=lambda *args : add(6) )
b6.place(x=134,y=85)
b1=Button(f1,text=1,font=('Helvetica',17),command=lambda *args : add(1) )
b1.place(x=30,y=156)
b2=Button(f1,text=2,font=('Helvetica',17),command=lambda *args : add(2) )
b2.place(x=82,y=156)
b3=Button(f1,text=3,font=('Helvetica',17),command=lambda *args :add(3) )
b3.place(x=134,y=156)
bC=Button(f1,text='C',bg='red',font=('Helvetica',17),command=lambda *args : memory.set(0) )
bC.place(x=30,y=230)
bzero=Button(f1,text='0',font=('Helvetica',17),command=lambda *args : add('0') )
bzero.place(x=82,y=230)
bdot=Button(f1,text='.',font=('Helvetica',17),command=lambda *args :add('.') )
bdot.place(x=134,y=230)

root.mainloop()