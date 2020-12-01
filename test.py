from tkinter import *


def gettext():
        print("hello")
        t1 = tt.get(1.0,END)
        print(type(t1))
        print(len(t1))
        print(t1)

root = Tk()

tt = Text(root,width=50,height=10)
tt.pack()

btnf = Frame(root)
btnf.pack()


btn1 = Button(btnf,text="ok",command=gettext)
btn1.pack()
root.mainloop()