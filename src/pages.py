import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import ImageTk, Image
import login
import register
import pandas as pd
import resep
import Shopper

class homePage :
    def __init__(self, root):
        self.root = root
        #setting title
        root.title("Home Page")
        #setting window size
        width=951
        height=703
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = "white")

        menuBar = tk.Frame(master = root, height = 50, width = 951, bg = "pink")
        menuBar.pack()

        labelTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelTitle["font"] = ft
        labelTitle["fg"] = "#333333"
        labelTitle["justify"] = "center"
        labelTitle["text"] = "Public Recipe"
        labelTitle["bg"] = "pink"
        labelTitle.config(font="Courier")
        labelTitle.place(x=378,y=10,width=205,height=30)

        labelSignUp=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelSignUp["font"] = ft
        labelSignUp["fg"] = "#333333"
        labelSignUp["justify"] = "center"
        labelSignUp["text"] = "Sign Up"
        labelSignUp["bg"] = "pink"
        labelSignUp.place(x=760,y=10,width=70,height=25)
        labelSignUp.bind("<Button-1>", self.gotoRegister)

        labelLogin=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelLogin["font"] = ft
        labelLogin["fg"] = "#333333"
        labelLogin["justify"] = "center"
        labelLogin["text"] = "Login"
        labelLogin["bg"] = "pink"
        labelLogin.place(x=840,y=10,width=70,height=25)
        labelLogin.bind("<Button-1>", self.gotoLogin)

        canvas = tk.Canvas(root, width = 300, height = 300, highlightthickness = 0)
        canvas.pack()
        canvas["bg"] = "white"
        img = ImageTk.PhotoImage(file = "../img/logo.jpg")
        canvas.create_image(60, 2, anchor = tk.NW, image = img)
        tk.mainloop()

    def gotoLogin(self, event) :
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Login(self.root)
        self.root.mainloop()

    def gotoRegister(self, event) :
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Register(self.root)
        self.root.mainloop()

class Login:
    def __init__(self, root):
        #setting title
        root.title("Login")
        #setting window size
        width=951
        height=703
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = "white")

        menuBar = tk.Frame(master = root, height = 50, width = 951, bg = "pink")
        menuBar.pack()

        labelTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelTitle["font"] = ft
        labelTitle["fg"] = "#333333"
        labelTitle["justify"] = "center"
        labelTitle["text"] = "Public Recipe"
        labelTitle["bg"] = "pink"
        labelTitle.config(font="Courier")
        labelTitle.place(x=378,y=10,width=205,height=30)

        entryUsername=tk.Entry(root)
        entryUsername["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryUsername["font"] = ft
        entryUsername["fg"] = "#333333"
        entryUsername["justify"] = "center"
        entryUsername["text"] = ""
        entryUsername["justify"] = "left"
        entryUsername.place(x=350,y=380,width=259,height=30)

        labelUsername=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelUsername["font"] = ft
        labelUsername["fg"] = "#333333"
        labelUsername["justify"] = "left"
        labelUsername["text"] = "Username :"
        labelUsername["bg"] = "white"
        labelUsername.place(x=350,y=350,width=68,height=30)

        labelPassword=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelPassword["font"] = ft
        labelPassword["fg"] = "#333333"
        labelPassword["justify"] = "left"
        labelPassword["text"] = "Password :"
        labelPassword["bg"] = "white"
        labelPassword.place(x=350,y=420,width=80,height=30)

        entryPassword=tk.Entry(root)
        entryPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryPassword["font"] = ft
        entryPassword["fg"] = "#333333"
        entryPassword["justify"] = "center"
        entryPassword["text"] = "tes"
        entryPassword["justify"] = "left"
        entryPassword.place(x=350,y=450,width=260,height=30)

        loginButton=tk.Button(root)
        loginButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        loginButton["font"] = ft
        loginButton["fg"] = "#000000"
        loginButton["justify"] = "center"
        loginButton["text"] = "Login"
        loginButton.place(x=450,y=510,width=70,height=25)
        loginButton["command"] = lambda : self.loginButton_command(root, entryUsername.get(), entryPassword.get(), comboBox.get())

        canvas = tk.Canvas(root, width = 300, height = 300, highlightthickness = 0)
        canvas.pack()
        canvas["bg"] = "white"
        img = ImageTk.PhotoImage(file = "../img/logo.jpg")
        canvas.create_image(60, 2, anchor = tk.NW, image = img)

        comboBox = ttk.Combobox(root, values = ["Shopper", "Pembeli"])
        comboBox.place(x = 410, y = 610)

        tk.mainloop()

    def loginButton_command(self, root, username, password, status):
        if status == "Pembeli" :
            registered = login.loginPembeli(username, password)
            if len(registered)>0 :
                root.destroy()
                root = tk.Tk()
                self.app = resep.Resep(root, username, password)
                root.mainloop()
            else :
                print("User tidak ditemukan")
                labelPassword=tk.Label(root)
                ft = tkFont.Font(family='Times',size=10)
                labelPassword["font"] = ft
                labelPassword["fg"] = "red"
                labelPassword["justify"] = "center"
                labelPassword["text"] = "Maaf, username/password salah"
                labelPassword["bg"] = "white"
                labelPassword.place(x=310,y=545,width=370,height=30)
        elif status == "Shopper" :
            registered = login.loginShopper(username, password)
            if registered :
                root.destroy()
                self.app = Shopper.shopperpage(username)
                
            else :
                print("User tidak ditemukan")

class Register:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=951
        height=703
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = "white")

        menuBar = tk.Frame(master = root, height = 50, width = 951, bg = "pink")
        menuBar.pack()

        labelTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelTitle["font"] = ft
        labelTitle["fg"] = "#333333"
        labelTitle["justify"] = "center"
        labelTitle["text"] = "Public Recipe"
        labelTitle["bg"] = "pink"
        labelTitle.config(font="Courier")
        labelTitle.place(x=378,y=10,width=205,height=30)

        labelName=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelName["font"] = ft
        labelName["fg"] = "#333333"
        labelName["justify"] = "left"
        labelName["text"] = "Name :"
        labelName.place(x=30,y=110,width=70,height=25)

        entryName=tk.Entry(root)
        entryName["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryName["font"] = ft
        entryName["fg"] = "#333333"
        entryName["justify"] = "center"
        entryName["text"] = ""
        entryName.place(x=30,y=140,width=303,height=30)

        labelPhone=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelPhone["font"] = ft
        labelPhone["fg"] = "#333333"
        labelPhone["justify"] = "left"
        labelPhone["text"] = "Phone :"
        labelPhone.place(x=30,y=180,width=70,height=25)

        entryPhone=tk.Entry(root)
        entryPhone["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryPhone["font"] = ft
        entryPhone["fg"] = "#333333"
        entryPhone["justify"] = "center"
        entryPhone["text"] = ""
        entryPhone.place(x=30,y=210,width=303,height=30)

        labelEmail=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelEmail["font"] = ft
        labelEmail["fg"] = "#333333"
        labelEmail["justify"] = "left"
        labelEmail["text"] = "Email address :"
        labelEmail.place(x=30,y=250,width=85,height=30)

        entryEmail=tk.Entry(root)
        entryEmail["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryEmail["font"] = ft
        entryEmail["fg"] = "#333333"
        entryEmail["justify"] = "center"
        entryEmail["text"] = ""
        entryEmail.place(x=30,y=280,width=303,height=30)

        labelAddress=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelAddress["font"] = ft
        labelAddress["fg"] = "#333333"
        labelAddress["justify"] = "left"
        labelAddress["text"] = "Address :"
        labelAddress.place(x=30,y=320,width=70,height=25)

        entryAddress=tk.Entry(root)
        entryAddress["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryAddress["font"] = ft
        entryAddress["fg"] = "#333333"
        entryAddress["justify"] = "center"
        entryAddress["text"] = ""
        entryAddress.place(x=30,y=350,width=303,height=30)

        labelUsername=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelUsername["font"] = ft
        labelUsername["fg"] = "#333333"
        labelUsername["justify"] = "left"
        labelUsername["text"] = "Username :"
        labelUsername.place(x=520,y=110,width=70,height=25)

        entryUsername=tk.Entry(root)
        entryUsername["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryUsername["font"] = ft
        entryUsername["fg"] = "#333333"
        entryUsername["justify"] = "center"
        entryUsername["text"] = ""
        entryUsername.place(x=520,y=140,width=303,height=30)

        labelPassword=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelPassword["font"] = ft
        labelPassword["fg"] = "#333333"
        labelPassword["justify"] = "left"
        labelPassword["text"] = "Password :"
        labelPassword.place(x=520,y=180,width=70,height=25)

        entryPassword=tk.Entry(root)
        entryPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryPassword["font"] = ft
        entryPassword["fg"] = "#333333"
        entryPassword["justify"] = "center"
        entryPassword["text"] = ""
        entryPassword.place(x=520,y=210,width=303,height=30)

        comboBox = ttk.Combobox(root, values = ["Shopper", "Pembeli"])
        comboBox.place(x = 603, y = 280)

        buttonRegister=tk.Button(root)
        buttonRegister["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        buttonRegister["font"] = ft
        buttonRegister["fg"] = "#000000"
        buttonRegister["justify"] = "center"
        buttonRegister["text"] = "Register"
        buttonRegister.place(x=640,y=310,width=70,height=25)
        buttonRegister["command"] = lambda : self.buttonRegister_command(root, entryName.get(), entryPhone.get(), entryEmail.get(), entryAddress.get(), entryUsername.get(), entryPassword.get(), comboBox.get())

    def buttonRegister_command(self, root, name, phone, email, address, username, password, status):
        if status == "Pembeli" :
            registered = register.registerPembeli(name, phone, email, address, username, password)
            if registered :
                root.destroy()
                root = tk.Tk()
                self.app = Login(root)
                root.mainloop()
            else :
                print("User telah pernah teregister")
        elif status == "Shopper" :
            registered = register.registerShopper(name, phone, email, address, username, password)    
            if registered :
                root.destroy()
                root = tk.Tk()
                self.app = Login(root)
                root.mainloop()
            else :
                print("User telah pernah teregister")







# from tkinter import *

# window = Tk()

# window.wm_attributes('-transparentcolor', 'black')

# homePage = Frame(master = window, height = 550, width = 2000)

# menuBar = Frame(master = homePage, height = 80, width = 2000, bg = "pink")
# labelTitle = Label(text = "Public Recipe", master = menuBar, justify = CENTER, bg = "pink")
# labelTitle.config(font=("Courier", 44))
# labelTitle.pack()
# menuBar.pack(fill = X, side = TOP, expand = False)

# frame = Frame(master = homePage, height = 2000, width = 2000, bg = "yellow")
# frame.pack(fill = BOTH, side = TOP, expand = False)

# homePage.pack(fill = BOTH, side = TOP, expand = True)

# window.mainloop()






# root = Tk()

# root.title("Public Recipe")
# menuBar = Frame(master = root, relief = RAISED, borderwidth = 1, bg = "pink", height = 20)

# menuBar.columnconfigure([0,1,2,3,4,5,6], minsize = 100, weight = 1)
# menuBar.rowconfigure(0, minsize = 20, weight = 1)

# labelTitle = Label(text = "Public Recipe", master = menuBar, justify = CENTER)
# labelTitle.grid(row = 0, column = 3, sticky = "ne")

# labelSignUp = Button(text = "Sign Up", master = menuBar, justify = RIGHT)
# labelSignUp.grid(row = 0, column = 6, sticky = "nw")

# labelLogin = Button(text = "Login", master = menuBar, justify = RIGHT)
# labelLogin.grid(row = 0, column = 6, sticky = "ne")

# menuBar.pack(fill = BOTH, expand = True)
# root.wm_attributes('-transparentcolor', 'black')

# root.mainloop()