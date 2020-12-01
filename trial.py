from tkinter import *
from functools import partial






def maketwt(twt,twt2,username):
    textt = twt.get(1.0,END)
    hasht = twt2.get(1.0,END)
    print(hasht)
    if(len(textt)==0):
        txt("Give some text")
    else:
        print(len(textt))
        a = NewTweet(client_socket,textt,hasht,username)
        if(a!=0):
            txt("tweeted successfully")
        else:
            txt("some error while tweeting")


def srcAux(twt,username):
    pass    
    



def SearchPersonv(username):
    global screen
    root = screen
    root.destroy()
    root = Tk()
    screen = root
    root.title("Mini Tweet")
    root.geometry("900x600")  
    # refresh1(root)
    frame1 = Frame(root)

    nt = partial(maketweetscreen,username)
    Button(frame1,text="NewTweet",command=nt).pack(side=LEFT)

    Button(frame1,text="Trending Hashtags").pack(side=LEFT)
    search11 = partial(SearchPersonv,username)
    Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
    Button(frame1,text="unfollow someone").pack(side=LEFT)
    Button(frame1,text="Search by Hastag").pack(side=LEFT)
    Button(frame1,text="Go to chatroom").pack(side=LEFT)
    Button(frame1,text="See own profile").pack(side=LEFT)
    frame1.pack(side=TOP)


    frame = Frame(root)
    twt = StringVar()
    twt = Text(frame, height = 10, width = 50)

    # twt2 = Text(frame,height =2,width = 50)
  
    tweet1 = partial(srcAux,twt,username)
    b1 = Button(frame,text="Search",command=tweet1)
    
    frame.pack()
    twt.pack()
    # twt2.pack()
    b1.pack()
    root.mainloop()

    
    
    
    



def maketweetscreen(username):
    global screen
    root = screen
    root.destroy()
    root = Tk()
    screen = root
    root.title("Mini Tweet")
    root.geometry("900x600")  
    # refresh1(root)
    frame1 = Frame(root)
    
    Button(frame1,text="Trending Hashtags").pack(side=LEFT)
    search11 = partial(SearchPersonv,username)
    Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
    Button(frame1,text="unfollow someone").pack(side=LEFT)
    Button(frame1,text="Search by Hastag").pack(side=LEFT)
    Button(frame1,text="Go to chatroom").pack(side=LEFT)
    Button(frame1,text="See own profile").pack(side=LEFT)
    frame1.pack(side=TOP)


    frame = Frame(root)
    twt = StringVar()
    twt = Text(frame, height = 10, width = 50)

    twt2 = Text(frame,height =2,width = 50)
  
    tweet1 = partial(maketwt,twt,twt2,username)
    b1 = Button(frame,text="Tweet",command=tweet1)
    
    frame.pack()
    twt.pack()
    twt2.pack()
    b1.pack()
    root.mainloop()


















































def Actionspage(username,arr):
    global screen
    root = screen
    root.destroy()
    root = Tk()

    screen = root
    root.title("Main Screen")
    root.geometry("900x600")
    # refresh1(root)
    frame1 = Frame(root)
    frame = Frame(root)
    nt = partial(maketweetscreen,username)
    Button(frame1,text="NewTweet",command=nt).pack(side=LEFT)


    Button(frame1,text="Trending Hashtags").pack(side=LEFT)
    Button(frame1,text="Search a person",command = SearchPersonv).pack(side=LEFT)
    Button(frame1,text="unfollow someone").pack(side=LEFT)
    Button(frame1,text="Search by Hastag").pack(side=LEFT)
    Button(frame1,text="Go to chatroom").pack(side=LEFT)
    Button(frame1,text="See own profile").pack(side=LEFT)
    frame1.pack(side=TOP)
    
    frame2 = Frame(root)

    frame2.pack(side=TOP)
    frame = Frame(root)
    Label(frame,text="").pack(side=TOP)
    scroll = Scrollbar(frame,orient=VERTICAL)
    myls = Listbox(frame,selectmode=EXTENDED,width=80,height=20,yscrollcommand=scroll.set,cursor="tcross")
    #config scrollbar
    scroll.config(command=myls.yview)
    scroll.pack(side=RIGHT,fill=Y)
    # myls.pack()
    frame.pack()
    myls.pack(pady=25,side=LEFT)
    
    # arr = Refresh(client_socket)

    # myls.insert(END,"Item")
    # myls.insert(END,"Item")
    # myls.insert(END,"Item")
    if(len(arr)!=0):
        for i in arr:
            myls.insert(END,i)
    #add items
    frame2 = Frame(root)
    frame2.pack()
    root.mainloop()
