from tkinter import *
from tracemalloc import start
from PIL import Image
from matplotlib import image

root=Tk()

file='pie.gif'
info=Image.open(file)
print('30')
frames=info.n_frames
print(frames)

im = [PhotoImage(file='pie.gif',format=f'gif -index {i}') for i in range(frames)]

print('14')
l1=Label(root,image='')
l1.pack()
count=0
anim=None
def animation(count=0):
    # print('16')
    global anim
    im2=im[count]
    l1.configure(image=im2)
    count+=1
    if count==frames:
        count=0
    anim=root.after(40 ,lambda : animation(count))
def stopper():
    global anim
    root.after_cancel(anim)

print('30')
start_button=Button(root,text='start',command=animation)
start_button.pack()
stop_button=Button(root,text='stop',command=stopper)
stop_button.pack()

root.mainloop()