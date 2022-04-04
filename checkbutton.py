from tkinter import *

root=Tk()
v1=IntVar(root)
c1=Checkbutton(root,text='green',onvalue=1,offvalue=0,variable=v1)
c1.pack()
l1=Label(root,text='0')
l1.pack()
def changer(*args):
     if v1.get() :
         l1.configure(text='1')
     else:
         l1.configure(text='0')
v1.trace('w', changer)

root.mainloop()