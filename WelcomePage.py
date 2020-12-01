from tkinter import *
from client_func import *
from functools import partial
import time
def callback(sv,len1):
    c = sv.get()[0:len1]
    # print("c=" , c)
    sv.set(c)

def Actionspage():
        root = screen
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
        Button(frame1,text="Log out",command=root.destroy).pack(side=LEFT)
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




def txt(frame,name):
    # tt1 = Label(screen,text="name is :"+name.get())
    tt1 = Tk()
    tt1.wm_title("!")
    label = Label(tt1,text = "Username entered is "+name.get(),font=("Calibri,15"))
    label.pack()
    B1 = Button(tt1,text="Okay",command=tt1.destroy)
    B1.pack()

    tt1.mainloop()






def register(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()
    
    frame = LabelFrame(screen,text="")

    Label(frame,pady=5,text="Please Enter your details",width="300",height=2,font=("Calibri",15)).pack()
    username = StringVar()
    username.trace("w", lambda name, index, mode, username=username: callback(username,20))    

    password = StringVar()
    password = password.trace("w", lambda name, index, mode, password=password: callback(password,20))
    
    name1 = StringVar()
    name1.trace("w", lambda name, index, mode, name1 =name1: callback(name1,20))

    email = StringVar()
    email.trace("w", lambda name, index, mode, email=email: callback(email,30))
    
    age = IntVar()
    
    gender = StringVar()
    gender.trace("w", lambda name, index, mode, gender=gender: callback(gender,1))
    
    institute = StringVar()
    institute.trace("w", lambda name, index, mode, institute=institute: callback(institute,30))
    
    status = StringVar()
    status.trace("w", lambda name, index, mode, status=status: callback(status,20))
    
    city = StringVar()
    city.trace("w", lambda name, index, mode, city=city: callback(status,20))
    
    
    
    Label(frame,text="Username").pack()
    username_entry = Entry(frame,textvariable=username)
    username_entry.pack()
    # Label(frame,text="").pack()

    Label(frame,text="Password").pack()
    password_entry = Entry(frame,textvariable=password,show="*")
    password_entry.pack()
    # Label(frame,text="").pack()

    Label(frame,text="Name").pack()
    name_entry = Entry(frame,textvariable=name1)
    name_entry.pack()
    # Label(frame,text="").pack()


    Label(frame,text="email").pack()
    email_entry = Entry(frame,textvariable=email)
    email_entry.pack()
    # Label(frame,text="").pack()




    Label(frame,text="gender").pack()
    gender_entry = Entry(frame,textvariable=gender)
    gender_entry.pack()
    # Label(frame,text="").pack()


    Label(frame,text="status").pack()
    status_entry = Entry(frame,textvariable=status)
    status_entry.pack()
    # Label(frame,text="").pack()


    Label(frame,text="city").pack()
    city_entry = Entry(frame,textvariable=city)
    city_entry.pack()    
    
    Label(frame,text="institute").pack()
    institute_entry = Entry(frame,textvariable=institute)
    institute_entry.pack()    
    
   
    Button(frame,text="Register",width=10,height=1,).pack()
    # Label(frame,text="").pack()

    mm = partial(txt,frame,username)
    Button(frame,text="Go to login",width=10,height=1,command=mm).pack() 
    
    frame.pack(expand="yes")  






def lloginpage(frame):
    # screen1 = Tk()
    # screen1.title("Minitweeter Login")
    # screen1.geometry("900x600")
    # Label(screen1,pady=25,text="Please Enter your details",width="300",height=2,font=("Calibri",15)).pack()
    # screen1.mainloop()

    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()

    frame = LabelFrame(screen,text="")
    Label(frame,pady=25,text="Please Enter your details",width="300",height=2,font=("Calibri",15)).pack()
    username = StringVar()
    password = StringVar()
    Label(frame,text="Username").pack()
    username_entry = Entry(frame,textvariable=username)
    username_entry.pack()
    Label(frame,text="Password").pack()
    password_entry = Entry(frame,textvariable=password,show="*")
    password_entry.pack()
    Label(frame,text="").pack()
    Button(frame,text="Login",width=10,height=1,command=screen.destroy).pack()
    Label(frame,text="").pack()

    mm = partial(main1,frame)
    Button(frame,text="goback",width=10,height=1,command=mm).pack()  
    frame.pack()  







    
    # pass
def main1(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()
    frame = LabelFrame(screen,text="",padx=2,pady=2)

    Label(frame,pady=50,text="Welcome To mini-twitter",width="300",height="2",font=("Calibri",40)).pack()
    # Label(pady=200,text="Welcome to twitter 2").pack()
    Label(frame,text="").pack()

    abc = partial(lloginpage,frame)
    Button(frame, text="Login",height="2",width="30",command=abc).pack()
    Label(frame, text="").pack()
    rr = partial(register,frame)
    Button(frame, text="Sign Up",height="2",width="30",command=rr).pack()
    Label(frame, text="").pack()
    
    
    # fwith_args = partial(with_args,1,2)
    
    # Button(frame, text="With Args",height="2",width="30",command=fwith_args).pack()
    # Label(frame, text="").pack()



    Button(frame, text="Quit",height="2",width="30",command=screen.destroy).pack()
    Label(frame, text="").pack()
    frame.pack()


    
    

def with_args(a,b):
    print("a+b:",a+b)


def main():
    global screen
    screen = Tk()
    screen.geometry("900x600")
    screen.title("Minitweeter")
    frame = LabelFrame(screen,text="",padx=2,pady=2)

    Label(frame,pady=50,text="Welcome To mini-twitter",width="300",height="2",font=("Calibri",40)).pack()
    # Label(pady=200,text="Welcome to twitter 2").pack()
    Label(frame,text="").pack()

    abc = partial(lloginpage,frame)
    Button(frame, text="Login",height="2",width="30",command=abc).pack()
    Label(frame, text="").pack()
    rr = partial(register,frame)
    Button(frame, text="Sign Up",height="2",width="30",command=rr).pack()
    Label(frame, text="").pack()
    
    
    # fwith_args = partial(with_args,1,2)
    
    # Button(frame, text="With Args",height="2",width="30",command=fwith_args).pack()
    # Label(frame, text="").pack()
    # Button(frame,text="Actionpage",height=2,width=30,command=Actionspage).pack()
    # Label(frame, text="").pack()


    Button(frame, text="Quit",height="2",width="30",command=screen.destroy).pack()
    Label(frame, text="").pack()
    
    
        
    frame.pack()
    screen.mainloop()



main()