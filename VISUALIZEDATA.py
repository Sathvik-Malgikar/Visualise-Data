from distutils import command
import imp
from tkinter import * 
from turtle import bgcolor, color
from matplotlib import image 

from matplotlib.pyplot import close, text
from numpy import var
from pyparsing import And, col
import piecreator
from PIL import ImageTk, Image
import pygame
import barcreator


def piechart():
    global vallist
    vallist=list(map(lambda n : n.get(),list_e))
    piecreator.pialg(vallist,list_l)
pygame.mixer.init()
pygame.mixer.music.load('Funky.mp3')
pygame.mixer.music.play()
def bargraph():
    global vallist
    vallist=list(map(lambda n : n.get(),list_e))
    barcreator.baralg(vallist)

no_of_items=0
def getter(from_return=False):
    global no_of_items
    if from_return :
        if input_in_e1.get()=='':
            pass
        else :
            no_of_items=int(input_in_e1.get())
            nextone()
    else:
        no_of_items=int(input_in_e1.get())
        nextone()
welcome=Tk()
welcome.state('zoomed')
welcome.geometry('800x600')
welcome.title('VISUALISE DATA')
textstring=open('textstring.txt','r')
Label(welcome,text=textstring.read(),font=('Helvetica','16')).pack()
Button(welcome,text='PROCEED',font=50,command=lambda : welcome.destroy(),height=4,width=17,bg='green').pack(pady=38)
gfl1=Label(welcome,image='')
gfl1.pack(side=LEFT)
gfl2=Label(welcome,image='')
gfl2.pack(side=RIGHT)

piefile='pie.gif'
pieimage=Image.open(piefile)
piegifframes=pieimage.n_frames
pie_im=[PhotoImage(file=piefile,format=f'gif -index {i}') for i in range(piegifframes)]
count=0
anim=None

barfile='bar.gif'
barimage=Image.open(barfile)
bargifframes=barimage.n_frames
bar_im=[PhotoImage(file=barfile,format=f'gif -index {i}') for i in range(bargifframes)]
# print(bargifframes,piegifframes)
def animation(count=0):
    global anim
    pim=pie_im[count]
    bim=bar_im[count]
    gfl1.configure(image=pim)
    gfl2.configure(image=bim)
    count+=1
    if count==piegifframes:
        count=0
    anim=welcome.after(40,lambda : animation(count))
animation()
welcome.mainloop()
textstring.close()
root=Tk()


root.geometry("1200x950")
root.title('VISUALISE DATA')
img = ImageTk.PhotoImage(Image.open("back.webp")) 
  

label1 = Label( root, image = img)
label1.place(x = 0, y = 0)


l1=Label(root,text='Number of items : ',font=100)
l1.grid(row=1,column=1,padx=60,pady=20)


input_in_e1 = StringVar(root)


e1=Entry(root, textvariable=input_in_e1)
e1.grid(row=1,column=2)
b1=Button(root,text='GO',command=getter)
b1.grid(row=1,column=3,padx=30)
def to_check():
    if input_in_e1.get().isdigit() :
        if len(input_in_e1.get()) > 0:
            b1.configure(state=NORMAL)
    else :
        b1.configure(state=DISABLED)
    

input_in_e1.trace('w', lambda *args : to_check())
to_check()

def nextone(save=None):
    def checking_last_field():
        if list_sv[-1].get()=='' :
            bargraph_button.configure(state=DISABLED)
            piechart_button.configure(state=DISABLED)
        else:
            bargraph_button.configure(state=NORMAL)
            piechart_button.configure(state=NORMAL)
    
    global list_l,list_e
    list_l=[]
    list_e=[]
    list_sv=[StringVar(root) for i in range(no_of_items)]
    for i in range(no_of_items):
        if save and i+1<no_of_items:
            list_sv[i].set(save[i].get())
        else:
             list_sv[i].set(0)
       
        list_l.append(Entry(root,font=50))
        list_l[i].insert(0, string=f'item {i+1} :')
        list_e.append(Entry(root,textvariable=list_sv[i]))
        
        list_l[i].grid(row=i+2,column=1,pady=10)
        list_e[i].grid(row=i+2,column=2,padx=7,pady=10)

    piechart_button=Button(root,text='CREATE PIECHART',command=piechart)
    piechart_button.grid(row=1,column=4,padx=30)
    bargraph_button=Button(root,text='CREATE BARGRAPH',command=bargraph)
    bargraph_button.grid(row=2,column=4,padx=30)
    checking_last_field()
    Label(root,font=50,text='Click enter to reset all the values',bg='green').grid(pady=10,row=70,column=1)
    list_sv[-1].trace('w', lambda * args: checking_last_field())
    def addone():
        global no_of_items
        no_of_items+=1
        input_in_e1.set(int(input_in_e1.get())+1)
        nextone(list_e)
    add_entry=Button(root,text='Add another entry',command=addone)
    add_entry.grid(column=1,row=30)

root.bind('<Return>',getter)

root.mainloop()
