from functools import partial
from tkinter import *


root = Tk()

root.title("fbwjkef")
root.geometry("900x600")
# #creating scrollbar
def Actionspage(root):
        root.destroy()
        root = Tk()
        root.title("fbwjkef")
        root.geometry("900x600")
        
        frame1 = Frame(root)
        Button(frame1,text="Hello").pack(side=LEFT)
        Button(frame1,text="NewTweet").pack(side=LEFT)
        Button(frame1,text="See Top trending").pack(side=LEFT)
        Button(frame1,text="Search a person").pack(side=LEFT)
        Button(frame1,text="unfollow someone").pack(side=LEFT)
        Button(frame1,text="Search Hastag").pack(side=LEFT)
        Button(frame1,text="Go to chat").pack(side=LEFT)
        Button(frame1,text="Log out").pack(side=LEFT)
        frame1.pack(side=TOP)

        frame = Frame(root)
        Label(frame,text="").pack(side=TOP)


        scroll = Scrollbar(frame,orient=VERTICAL)



        myls = Listbox(frame,selectmode=EXTENDED,width=80,height=20,yscrollcommand=scroll.set)

        #config scrollbar

        scroll.config(command=myls.yview)
        scroll.pack(side=RIGHT,fill=Y)

        # myls.pack()
        frame.pack()


        myls.pack(pady=25,side=LEFT)
        def delete_list(myls):
                print(ANCHOR)
                print(type(ANCHOR))
                myls.delete(ANCHOR)

        arr = ["one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three","one","two","three"]
        myls.insert(END,"Item")
        myls.insert(END,"Item")
        myls.insert(END,"Item")

        for i in arr:
                myls.insert(END,i)


        #add items
        frame2 = Frame(root)

        frame2.pack()
        root.mainloop()


Actionspage(root)





